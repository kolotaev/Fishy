from unittest import TestCase
from unittest.mock import Mock, patch

from app.model.words import *


class TestWordsModel(TestCase):
    @patch('app.model.words.CsvFileWords')
    def test_create_model(self, csv_file_words_mock):
        c = Mock()
        create_model(c)
        csv_file_words_mock.assert_called_once()
