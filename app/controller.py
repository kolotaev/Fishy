import threading
import os.path
import tkinter as tk
from datetime import datetime

from .configurator import Config
from .view.root import MainFrame
from .view.front import ExplainText
from .consts import CONF_FILE_NAME, TIME_FORMAT
from .model.words import create_model
from .providers.speech import create_speech_provider
from .providers.translation import create_translation_provider


class Application:
    @staticmethod
    def launch(config_file=CONF_FILE_NAME):
        if config_file.startswith('~'):
            config_path = os.path.join(os.path.expanduser('~'), config_file)
        else:
            config_path = config_file
        conf = Config(config_path, create=True)
        conf.init()
        controller = Controller(
            create_model(conf),
            MainFrame(conf),
            create_speech_provider(conf),
            create_translation_provider(conf),
            conf
        )
        controller.start()


class Controller:
    def __init__(self, model, view, speech_provider, translation_provider, config):
        self.model = model
        self.view = view
        self.config = config
        self.view.on_close(self.stop)
        self.speech_provider = speech_provider
        self.translation_provider = translation_provider
        self.showing_thread = ShowingThread(view, self.config)
        self.view.hide_btn.config(command=view.hide)
        self.view.back_btn.config(command=self._show_previous)
        self.view.forward_btn.config(command=self._show_next)
        self.view.speak_btn_one.config(command=self._speak_current_word)
        self.view.speak_btn_all.config(command=self._speak_current_definition)
        self.view.additional_translate_btn_one.config(command=self._show_additional_translate_current_word)
        self.view.additional_translate_btn_all.config(command=self._show_additional_translate_current_definition)

    def start(self):
        self.showing_thread.start()
        self.view.show()
        self._show_current()
        self.view.loop()

    def stop(self):
        self.showing_thread.terminate()

    def _show_explain(self, evt, txt=None):
        self.view.explain_text.config(state=tk.NORMAL)
        self.view.explain_text.insert(tk.END, txt)
        self.view.explain_text.config(state=tk.DISABLED)

    def _hide_explain(self, *args):
        self.view.explain_text.config(state=tk.NORMAL)
        self.view.explain_text.delete('1.0', tk.END)
        self.view.explain_text.config(state=tk.DISABLED)

    def _show_current(self):
        self._show(self.model.get_current())

    def _show_next(self):
        self._show(self.model.get_next())

    def _show_previous(self):
        self._show(self.model.get_previous())

    def _show(self, entry):
        def explain_view(data, fun):
            return lambda evt: fun(evt, data)
        if not entry:
            return
        self.view.word_label.config(text='%s. %s' % (entry.number, entry.word))
        explain_text = (ExplainText(entry).txt())
        if self.model.is_current_a_repeat():
            self.view.explain_text.bind("<Enter>", explain_view(explain_text, self._show_explain))
            self.view.explain_text.bind("<Leave>", explain_view(explain_text, self._hide_explain))
            self._hide_explain(None)
        else:
            self.view.explain_text.unbind("<Enter>")
            self.view.explain_text.unbind("<Leave>")
            self._show_explain(None, explain_text)

    def _speak_current_word(self):
        word = self.model.get_current().word
        self.speech_provider.speak(word)

    def _speak_current_definition(self):
        text = self.model.get_current().definition + self.model.get_current().examples
        self.speech_provider.speak(text)

    def _show_additional_translate_current_word(self):
        word = self.model.get_current().word
        tr = self.translation_provider.translate(word, all_possible=True)
        self.view.modal.show(word, tr)

    def _show_additional_translate_current_definition(self):
        text = "%s\n%s" % (self.model.get_current().definition, self.model.get_current().examples)
        tr = self.translation_provider.translate(text)
        self.view.modal.show(text, tr)


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
                if self.within_allowed_time():
                    self.win.show()
                self.stop.wait(timeout)
        finally:
            self._running_flag = False

    def terminate(self):
        self.stop.set()

    def within_allowed_time(self):
        start_time_str = self.config.get('popup', 'start_time')
        start_time = datetime.strptime(start_time_str, TIME_FORMAT).time()
        end_time_str = self.config.get('popup', 'end_time')
        end_time = datetime.strptime(end_time_str, TIME_FORMAT).time()
        return start_time <= self._current_time() <= end_time

    @staticmethod
    def _current_time():
        return datetime.today().time()
