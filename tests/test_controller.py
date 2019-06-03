from unittest import TestCase
from unittest.mock import Mock

from app.controller import Controller
from app.view.root import MainFrame


class TestController(TestCase):
    def test_start(self):
        model = Mock()
        view = Mock(spec=MainFrame)
        showing_th = Mock()
        cf = Controller(model, view, Mock)
        cf.showing_thread = showing_th
        cf.start()
        showing_th.start.assert_called_once()
        view.show.assert_called_once()
        view.loop.assert_called_once()

    def test_stop(self):
        model = Mock()
        view = Mock(spec=MainFrame)
        showing_th = Mock()
        cf = Controller(model, view, Mock)
        cf.showing_thread = showing_th
        cf.stop()
        showing_th.terminate.assert_called_once()
