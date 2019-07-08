import csv
import os.path

from .repeat import create_strategy
from ..util import sanitize


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


# todo - get translations from provider
class WordsDatabase:
    """
    Takes words from a database.
    Saves current word position into config file.
    Class should be overridden to get words from a proper database
    """
    def __init__(self, config):
        self.config = config
        self._new_learn = self.config.getint('run', 'new-word-pointer', fallback=1)
        self._current = self.config.getint('run', 'current-pointer', fallback=1)
        self._repeat_counter = self.config.getint('run', 'repeat-counter', fallback=0)
        self.repeat_intensity = self.config.getint('learn', 'repeat-intensity')
        self.repeat_strategy = create_strategy(config)
        self.db = {}

    def get_current(self):
        return self._entry_by_number(self._current)

    def get_next(self):
        if self._is_repeat():
            self._repeat_counter += 1
            self._current = self.repeat_strategy.next(self._new_learn, self._repeat_counter)
        elif self._current < len(self.db):
            self._repeat_counter = 0
            self._new_learn += 1
            self._current = self._new_learn
        return self.get_current()

    def get_previous(self):
        if self._is_repeat() and self._repeat_counter > 0:
            self._repeat_counter -= 1
            self._current = self.repeat_strategy.next(self._new_learn, self._repeat_counter)
        elif self._current >= 0:
            self._new_learn -= 1
            self._current = self._new_learn
        return self.get_current()

    def is_current_a_repeat(self):
        return self._repeat_counter != 0

    def save(self):
        self.config.save('run', 'new-word-pointer', self._new_learn)
        self.config.save('run', 'current-pointer', self._current)
        self.config.save('run', 'repeat-counter', self._repeat_counter)

    def _is_repeat(self):
        return self._repeat_counter < self.repeat_intensity

    def _entry_by_number(self, number):
        return self.db.get(number)


class CsvFileWords(WordsDatabase):
    """
    CSV file database
    """
    def __init__(self, config):
        super().__init__(config)
        file = os.path.expanduser(self.config.get('corpus', 'file_path'))
        if not os.path.exists(file):
            raise Exception('CSV file "%s" with corpus does not exist' % file)
        with open(file) as csv_data_file:
            dialect = csv.Sniffer().sniff(csv_data_file.read(1024))
            csv_data_file.seek(0)
            csv_reader = csv.DictReader(csv_data_file, dialect=dialect)
            for row in csv_reader:
                num = int(row['number'])
                row['examples'] = sanitize(row['examples'])
                row['definition'] = sanitize(row['definition'])
                self.db[num] = Entry(**row)
