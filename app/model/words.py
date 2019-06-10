

class WordsDatabase:
    def __init__(self, config):
        self.config = config
        self.current = 0

    def get_next(self):
        self.current += 1
        return self.current

    def get_previous(self):
        self.current -= 1
        return self.current
