import tkinter as tk


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
        self._add_word_label()
        self._add_explain_text()
        self._add_controls()
        self.frame.pack(fill=tk.BOTH)

    def _add_word_label(self):
        word_label = tk.Label(self.frame, font=("Courier", 22),
                              text="Юникод очень длинное слово",
                              height=4)
        word_label.pack(fill=tk.BOTH, padx=16, pady=4, ipadx=4, ipady=4)
        # Expose to main view
        self.app.word_label = word_label

    def _add_explain_text(self):
        txt = tk.Text(self.frame,
                      background='#f6f6f6', font=('Courier', 14),
                      padx=12, pady=12, wrap=tk.WORD)
        txt.insert(tk.END, 'What is Lorem Ipsum?')
        txt.pack(fill=tk.BOTH, padx=16, pady=4, ipadx=4, ipady=10)
        txt.config(state=tk.DISABLED)
        # Expose to main view
        self.app.explain_text = txt

    def _add_controls(self):
        controls_frame = tk.Frame(self.frame)
        hide_btn = tk.Button(controls_frame, width=10, text='Hide')
        back_btn = tk.Button(controls_frame, width=10, text='<<')
        forward_btn = tk.Button(controls_frame, width=10, text='>>')
        hide_btn.pack(side=tk.BOTTOM, pady=10, padx=10)
        back_btn.pack(side=tk.LEFT, pady=10, padx=10)
        forward_btn.pack(side=tk.RIGHT, pady=10, padx=10)
        controls_frame.pack(side=tk.BOTTOM, fill=tk.X, expand=True)
        # Expose controls to main view
        self.app.hide_btn = hide_btn
        self.app.back_btn = back_btn
        self.app.forward_btn = forward_btn
