import tkinter as tk


class Front:
    def __init__(self, app, config):
        self.frame = tk.Frame(app.win)
        self.app = app
        self.conf = config

    def add(self):
        tk.Label(self.frame, font=("Courier", 22), text="Юникод очень длинное слово",
                 width=150, height=10).pack()
        tk.Message(self.frame, borderwidth=10,
                   background='grey', text="Translated! gjhgjhg jg j").pack(fill=tk.BOTH)
        tk.Button(self.frame, padx=10, pady=5, text='Hide', command=self.app.hide).pack(expand=True)
        self.frame.pack()
