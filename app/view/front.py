import tkinter as tk


class Front:
    def __init__(self, app, config):
        self.frame = tk.Frame(app.win)
        self.app = app
        self.conf = config

    def add(self):
        self._add_word_label()
        self._add_explain_text()
        # self._add_examples_text()
        self._add_controls()
        self.frame.pack(fill=tk.BOTH)

    def _add_word_label(self):
        tk.Label(self.frame,
         font=("Courier", 22),
         text="Юникод очень длинное слово",
         # width=150,
         height=4,
         ).pack(fill=tk.BOTH,
                padx=16,
                pady=4,
                ipadx=4,
                ipady=4)

    def _add_explain_text(self):
        txt = tk.Text(self.frame,
                      background='#e9e6e8',
                      font=("Courier", 14),
                      padx=12,
                      pady=12,
                      wrap=tk.WORD,
                      )
        txt.insert(tk.END, 'What is Lorem Ipsum?')
        txt.pack(
            fill=tk.BOTH,
            padx=16,
            pady=4,
            ipadx=4,
            ipady=10
        )
        txt.config(state=tk.DISABLED)

    def _add_examples_text(self):
        txt = tk.Text(self.frame,
                      background='#e9e6e8',
                      font=("Courier", 14),
                      padx=12,
                      pady=12,
                      wrap=tk.WORD,
                      )
        txt.insert(tk.END, 'What is Lorem Ipsum?')
        txt.pack(
            fill=tk.BOTH,
            padx=16,
            pady=4,
            ipadx=4,
            ipady=10
        )
        txt.config(state=tk.DISABLED)

    def _add_controls(self):
        controls_frame = tk.Frame(self.frame)
        b1 = tk.Button(controls_frame,
                       width=10,
                       fg='yellow',
                       text='Hide',
                       command=self.app.hide)
        b2 = tk.Button(controls_frame,
                       width=10,
                       text='<<',
                       command=self.app.hide)
        b3 = tk.Button(controls_frame,
                       width=10,
                       text='>>',
                       command=self.app.hide)
        b1.pack(
            side=tk.BOTTOM,
            pady=10, padx=10
        )
        b2.pack(
            side=tk.LEFT,
            pady=10, padx=10
        )
        b3.pack(
            side=tk.RIGHT,
            pady=10, padx=10
        )
        controls_frame.pack(side=tk.BOTTOM, fill=tk.X, expand=True)
