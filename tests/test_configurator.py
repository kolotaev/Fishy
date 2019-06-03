import unittest
from unittest.mock import Mock

from app.configurator import Config


class TestConfigurator(unittest.TestCase):
    def test_get_show_timeout(self):
        cf = Config('foo.cnf', create=False)
        for val, unit, expect in [
            (10, 'hour', 36000),
            (1, 'sec', 1),
            (4, 'unknown', 4),
            (4, 'min', 240),
        ]:
            cf.getint = Mock()
            cf.getint.return_value = val
            cf.get = Mock()
            cf.get.return_value = unit
            # asserts
            res = cf.get_show_timeout()
            self.assertEqual(expect, res)
            cf.get.assert_called_once_with('popup', 'show_timeout_unit')
            cf.getint.assert_called_once_with('popup', 'show_timeout_value')

    def test_init_creates_if_missing(self):
        cf = Config('foo.cnf', create=True)
        cf.create_if_missing = Mock()
        cf.read = Mock()
        cf.init()
        cf.create_if_missing.assert_called_once()
        cf.read.assert_called_once()

    def test_init_does_not_create_if_missing(self):
        cf = Config('foo.cnf')
        cf.create_if_missing = Mock()
        cf.read = Mock()
        cf.init()
        cf.create_if_missing.assert_not_called()
        cf.read.assert_called_once()
