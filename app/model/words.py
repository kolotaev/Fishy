from abc import ABCMeta


def create_model(config):
    # Currently this factory returns only one type of model
    return JsonFileWords(config)


class WordsDatabase(metaclass=ABCMeta):
    def get_next(self):
        pass

    def get_previous(self):
        pass


class JsonFileWords(WordsDatabase):
    """
    Takes words from a database file.
    Saves current word position into config file.
    """
    def __init__(self, config):
        self.config = config
        self.current = 0

    def get_next(self):
        self.current += 1
        return self.current

    def get_previous(self):
        self.current -= 1
        return self.current
