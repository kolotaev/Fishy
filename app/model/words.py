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
        self.part = kwargs['part'] or None
        self.transcription = kwargs['transcription'] or None
        self._definition = kwargs['definition'] or None
        self._examples = kwargs['examples'] or None
        self._picture_url = kwargs['picture'] or None

    @staticmethod
    def _sanitize(data):
        return data.replace('"\\n"', '\n')

    @property
    def definition(self):
        return self._sanitize(self._definition)

    @property
    def examples(self):
        return self._sanitize(self._examples)


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
        self._current = self.config.getint('corpus', 'current')
        file = os.path.expanduser(self.config.get('corpus', 'file_path'))
        self.db = {}
        if not os.path.exists(file):
            raise Exception('File does not exist')
        with open(file) as csv_data_file:
            dialect = csv.Sniffer().sniff(csv_data_file.read(1024))
            csv_data_file.seek(0)
            csv_reader = csv.DictReader(csv_data_file, dialect=dialect)
            for row in csv_reader:
                print(row)
                self.db[int(row['number'])] = Entry(**row)

    @property
    def current(self):
        return self.db.get(self._current)

    def get_current(self):
        return self.current

    def get_next(self):
        self._current += 1
        return self.current

    def get_previous(self):
        self._current -= 1
        return self.current
