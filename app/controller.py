import threading
import os.path

from .configurator import Config
from .view.root import MainFrame
from .consts import CONF_FILE_NAME


class Application:
    @staticmethod
    def launch():
        config_path = os.path.join(os.path.expanduser('~'), CONF_FILE_NAME)
        conf = Config(config_path, create=True)
        conf.init()
        controller = Controller(None, MainFrame(conf), conf)
        controller.start()


class Controller:
    def __init__(self, model, view, config):
        self.model = model
        self.view = view
        self.config = config
        self.view.on_close(self.stop)
        self.showing_thread = ShowingThread(view, self.config)
        self.view.hide_btn.config(command=view.hide)
        self.view.back_btn.config(command=view.hide)
        self.view.forward_btn.config(command=view.hide)

    def start(self):
        self.showing_thread.start()
        self.view.show()
        self.view.loop()

    def stop(self):
        print('killing...')
        self.showing_thread.terminate()


class ShowingThread(threading.Thread):
    def __init__(self, win, config):
        self.win = win
        self.config = config
        self._running_flag = False
        self.stop = threading.Event()
        super().__init__()

    def run(self):
        timeout = self.config.get_show_timeout()
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
