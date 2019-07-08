import tkinter as tk


class ExplainText:
    def __init__(self, entry):
        self.entry = entry

    def txt(self):
        exp = self._wrap(self.entry.part)
        if self.entry.transcription:
            exp += '[%s]' % self.entry.transcription
        exp += self._wrap(self.entry.definition)
        exp += '\n%s' % self.entry.examples
        return exp

    @staticmethod
    def _wrap(word):
        return '\n%s\n\n' % word + '-' * 30 + '\n\n'


class Front:
    """
    Contains all the elements of learning: word, explanation.
    Also contains needed controls.
    All the elements are exposed and available in the root application window.
    """
    def __init__(self, app, config):
        self.frame = tk.Frame(app.win)
        self.app = app
        self.conf = config
        self.controls = []

    def add(self):
        self._add_controls()
        self._add_word_label()
        self._add_explain_text()
        self.frame.pack(fill=tk.BOTH)

    def _add_word_label(self):
        font = (self.conf.get('window', 'word-font-family'), self.conf.get('window', 'word-font-size'))
        word_label = tk.Label(self.frame, font=font, height=4)
        word_label.pack(fill=tk.BOTH, padx=16, pady=4, ipadx=4, ipady=4)
        # Expose to main view
        self.app.word_label = word_label

    def _add_explain_text(self):
        font = (self.conf.get('window', 'explain-font-family'), self.conf.get('window', 'explain-font-size'))
        txt = tk.Text(self.frame,
                      background='#f6f6f6', font=font,
                      padx=12, pady=12, wrap=tk.WORD)
        txt.pack(fill=tk.BOTH, padx=16, pady=4, ipadx=4, ipady=10)
        txt.config(state=tk.DISABLED)
        # Expose to main view
        self.app.explain_text = txt

    def _add_controls(self):
        controls_frame = tk.Frame(self.frame)
        # declare buttons
        hide_btn = tk.Button(controls_frame, width=10, text='Hide')
        back_btn = tk.Button(controls_frame, width=10, text='<<')
        forward_btn = tk.Button(controls_frame, width=10, text='>>')
        speak_btn_one = tk.Button(controls_frame, width=10, text='(*)')
        speak_btn_all = tk.Button(controls_frame, width=10, text='((*))')
        additional_translate_btn_one = tk.Button(controls_frame, width=10, text='trslt word')
        additional_translate_btn_all = tk.Button(controls_frame, width=10, text='trslt all')
        # pack buttons
        hide_btn.pack(side=tk.BOTTOM, pady=0, padx=10)
        back_btn.pack(side=tk.LEFT, pady=0, padx=10)
        speak_btn_all.pack(side=tk.LEFT, pady=0, padx=10)
        speak_btn_one.pack(side=tk.LEFT, pady=0, padx=10)
        additional_translate_btn_one.pack(side=tk.LEFT, pady=0, padx=10)
        additional_translate_btn_all.pack(side=tk.LEFT, pady=0, padx=10)
        forward_btn.pack(side=tk.RIGHT, pady=0, padx=10)
        controls_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # expose controls to main view
        self.app.hide_btn = hide_btn
        self.app.back_btn = back_btn
        self.app.forward_btn = forward_btn
        self.app.speak_btn_one = speak_btn_one
        self.app.speak_btn_all = speak_btn_all
        self.app.additional_translate_btn_one = additional_translate_btn_one
        self.app.additional_translate_btn_all = additional_translate_btn_all
