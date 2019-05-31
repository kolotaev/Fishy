import unittest
from unittest.mock import Mock, patch

from app.configurator import get_show_timeout, config


class TestConfigurator(unittest.TestCase):
    def test_get_show_timeout(self):
        with patch(config) as mock_config:
            mock_config.getint.return_value = 10
            mock_config.get.return_value = 'hour'
            self.assertEqual(get_show_timeout(), 60)
