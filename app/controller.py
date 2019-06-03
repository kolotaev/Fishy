import threading

from .configurator import init, get_show_timeout
from .view.root import MainFrame


class Application:
    @staticmethod
    def launch():
        init()
        controller = Controller(None, MainFrame())
        controller.start()


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.on_close(self.stop)
        self.showing_thread = ShowingThread(view)

    def start(self):
        self.showing_thread.start()
        self.view.show()
        self.view.loop()

    def stop(self):
        print('killing...')
        self.showing_thread.terminate()


class ShowingThread(threading.Thread):
    def __init__(self, win):
        self.win = win
        self._running_flag = False
        self.stop = threading.Event()
        super().__init__()

    def run(self):
        timeout = get_show_timeout()
        try:
            while not self.stop.wait(0):
                self._running_flag = True
                print("Waiting for %d secs..." % timeout)
                if self.win.is_alive:
                    self.win.show()
                self.stop.wait(timeout)
        finally:
            self._running_flag = False

    def terminate(self):
        self.stop.set()
