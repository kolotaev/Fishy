from abc import ABCMeta
import csv
import os.path


def create_model(config):
    # Currently this factory returns only one type of model
    return CsvFileWords(config)


class Entry:
    def __init__(self, **kwargs):
        self.number = kwargs['number'] or None
        self.word = kwargs['word'] or None
        self._part = kwargs['part'] or None
        self.transcription = kwargs['transcription'] or None
        self._definition = kwargs['definition'] or None
        self._examples = kwargs['examples'] or None
        self._picture_url = kwargs['picture'] or None

    @staticmethod
    def _sanitize(data):
        if data is None:
            data = ''
        return str(data).replace('"\\n"', '\n')

    @property
    def part(self):
        return self._sanitize(self._part)

    @property
    def definition(self):
        return self._sanitize(self._definition)

    @property
    def examples(self):
        return self._sanitize(self._examples)


class WordsDatabase(metaclass=ABCMeta):
    def current(self):
        pass

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
        self._current = self.config.getint('learn', 'current')
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

    @property
    def current(self):
        return self._current

    def get_current(self):
        return self.db.get(self.current)

    def get_next(self):
        if self._current < self._max:
            self._current += 1
        return self.get_current()

    def get_previous(self):
        if self._current > 1:
            self._current -= 1
        return self.get_current()
