import threading
import os.path
import tkinter as tk

from .configurator import Config
from .view.root import MainFrame
from .consts import CONF_FILE_NAME
from .model.words import WordsDatabase


class Application:
    @staticmethod
    def launch():
        config_path = os.path.join(os.path.expanduser('~'), CONF_FILE_NAME)
        conf = Config(config_path, create=True)
        conf.init()
        controller = Controller(WordsDatabase(conf), MainFrame(conf), conf)
        controller.start()


class Controller:
    def __init__(self, model, view, config):
        self.model = model
        self.view = view
        self.config = config
        self.view.on_close(self.stop)
        self.showing_thread = ShowingThread(view, self.config)
        self.view.hide_btn.config(command=view.hide)
        self.view.back_btn.config(command=self._show_next)
        self.view.forward_btn.config(command=self._show_previous)
        self.view.explain_text.bind("<Enter>", self._show_explain)
        self.view.explain_text.bind("<Leave>", self._hide_explain)

    def start(self):
        self.showing_thread.start()
        self.view.show()
        self.view.loop()

    def stop(self):
        print('killing...')
        self.showing_thread.terminate()

    def _show_explain(self, evt):
        self._add_to_expain('aa?\n')

    def _hide_explain(self, evt):
        self._add_to_expain('bb?\n')

    def _show_next(self):
        self.view.word_label.config(text=self.model.get_next())

    def _show_previous(self):
        self.view.word_label.config(text=self.model.get_previous())

    def _add_to_expain(self, txt):
        self.view.explain_text.config(state=tk.NORMAL)
        self.view.explain_text.insert(tk.END, txt)
        self.view.explain_text.config(state=tk.DISABLED)


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
