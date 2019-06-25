from abc import ABCMeta
from random import randint


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
    """
    Example:
    current = 70
    repeat-counter = -> 1, 2, 3
    next gives: 69, 68, 67
    """
    def next(self, current, repeat_counter):
        n = current - repeat_counter
        if n < 0:
            return repeat_counter
        return n


class LongStepsBackStrategy(Strategy):
    """
    Example:
    current = 700
    repeat-counter = -> 1, 2, 3
    words-repeat = 30
    repeat-intensity = 3
    next gives: 670, 640, 610
    If step gives less than 0 -> returns random pointer till current position.
    """
    def next(self, current, repeat_counter):
        step_back_word_pointer = current - self.repeat_words * repeat_counter
        if step_back_word_pointer > 0:
            return step_back_word_pointer
        return randint(1, current-1)
