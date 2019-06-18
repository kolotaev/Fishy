from unittest import TestCase
from unittest.mock import Mock, PropertyMock, patch
from datetime import datetime

from app.controller import Controller, ShowingThread
from app.configurator import Config


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


class TestShowingThread(TestCase):
    def test_within_allowed_time(self):
        cf = Config('foo.cnf', create=False)
        showing_th = ShowingThread(win=None, config=cf)
        for start, end, now, expect in [
            ('12.00', '14.00', '1997-07-16T19:20:00', False),
            ('12.00', '22.00', '1997-07-16T19:20:00', True),
            ('21.00', '23.59', '1997-07-16T19:20:00', False),
            ('00.00', '00.00', '1997-07-16T19:20:00', False),
        ]:
            def get_side_effect(*args):
                if args == ('popup', 'start_time'):
                    return start
                elif args == ('popup', 'end_time'):
                    return end
            cf.get = Mock()
            cf.get.side_effect = get_side_effect
            showing_th._current_time = Mock(
                return_value=datetime.strptime(now, "%Y-%m-%dT%H:%M:%S").time()
            )
            # asserts
            self.assertEqual(expect, showing_th.within_allowed_time())
