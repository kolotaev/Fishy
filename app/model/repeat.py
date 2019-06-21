from abc import ABCMeta


def create_strategy(config):
    if config.get('learn', 'repeat-strategy') == 'long-steps-back':
        return LongStepsBackStrategy(config)
    return OneStepBackStrategy(config)


class Strategy(metaclass=ABCMeta):
    def __init__(self, config):
        self.repeat_words = config.getint('learn', 'words-repeat')

    def next(self, current, repeat_counter):
        pass


class OneStepBackStrategy(Strategy):
    def next(self, current, repeat_counter):
        n = current - repeat_counter
        if n < 0:
            return repeat_counter
        return n


class LongStepsBackStrategy(Strategy):
    def next(self, current, repeat_counter):
        return (current - self.repeat_words) + repeat_counter
