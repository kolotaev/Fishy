from abc import ABCMeta
import csv
import os.path

from .repeat import create_strategy


def create_model(config):
    # Currently this factory returns only one type of model
    return CsvFileWords(config)


class Entry:
    def __init__(self, **kwargs):
        self.number = kwargs['number'] or None
        self.word = kwargs['word'] or None
        self.part = kwargs['part'] or None
        self.transcription = kwargs['transcription'] or None
        self.definition = kwargs['definition'] or None
        self.examples = kwargs['examples'] or None
        self.picture_url = kwargs['picture'] or None


class WordsDatabase(metaclass=ABCMeta):
    def get_current(self):
        pass

    def get_next(self):
        pass

    def get_previous(self):
        pass


class CsvFileWords(WordsDatabase):
    """
    Takes words from a database file.
    Saves current word position into config file.
    """
    def __init__(self, config):
        self.config = config
        self._current = self.config.getint('run', 'current-pointer')
        self._repeat_counter = self.config.getint('run', 'repeat-counter')
        self.repeat_intensity = self.config.getint('learn', 'repeat-intensity')
        self.repeat_strategy = create_strategy(config)
        file = os.path.expanduser(self.config.get('corpus', 'file_path'))
        self.db = {}
        if not os.path.exists(file):
            raise Exception('CSV file "%s" with corpus does not exist' % file)
        with open(file) as csv_data_file:
            dialect = csv.Sniffer().sniff(csv_data_file.read(1024))
            csv_data_file.seek(0)
            csv_reader = csv.DictReader(csv_data_file, dialect=dialect)
            for row in csv_reader:
                num = int(row['number'])
                self.db[num] = Entry(**row)
                self._max = num

    def get_current(self):
        return self._get_word_by_number(self._current)

    def get_next(self):
        if self._is_repeat():
            self._repeat_counter += 1
            next_repeat = self.repeat_strategy.next(self._current, self._repeat_counter)
            return self._get_word_by_number(next_repeat)
        else:
            self._repeat_counter = 0
        if self._current < self._max:
            self._current += 1
        return self.get_current()

    def get_previous(self):
        if self._current > 1:
            self._current -= 1
        return self.get_current()

    def is_current_a_repeat(self):
        return self._repeat_counter != 0

    def save(self):
        self.config.save('run', 'current-pointer', self._current)
        self.config.save('run', 'repeat-counter', self._repeat_counter)

    def _is_repeat(self):
        return self._repeat_counter < self.repeat_intensity

    def _get_word_by_number(self, number):
        return self.db.get(number)
