from unittest import TestCase
from unittest.mock import Mock, PropertyMock

from app.controller import Controller


class TestController(TestCase):
    def test_start(self):
        model = Mock()
        view = PropertyMock()
        showing_th = Mock()
        ctrl = Controller(model, view, Mock())
        ctrl.showing_thread = showing_th
        ctrl.start()
        showing_th.start.assert_called_once()
        view.show.assert_called_once()
        view.loop.assert_called_once()

    def test_stop(self):
        model = Mock()
        view = PropertyMock()
        showing_th = Mock()
        ctrl = Controller(model, view, Mock())
        ctrl.showing_thread = showing_th
        ctrl.stop()
        showing_th.terminate.assert_called_once()
