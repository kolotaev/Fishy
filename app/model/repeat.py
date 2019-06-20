from abc import ABCMeta


def create_strategy(config):
    if config.get('learn', 'repeat-strategy') == 'long-circles':
        return LongCirclesStrategy(config)


class Strategy(metaclass=ABCMeta):
    def next(self, current, repeat_counter):
        pass


class LongCirclesStrategy(Strategy):
    def __init__(self, config):
        self.repeat_words = config.getint('learn', 'words-repeat')

    def next(self, current, repeat_counter):
        return (current - self.repeat_words) + repeat_counter
