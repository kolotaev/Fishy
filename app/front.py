import tkinter as tk


class Front:
    def __init__(self, parent):
        pw = parent.win
        self.source = tk.Label(pw, padx=100, pady=50, text="Word!")
        self.trans = tk.Message(pw, padx=100, background='grey', pady=50, text="Translated!")
        self.hide_btn = tk.Button(pw, text='Hide', command=parent.hide)

    def show(self):
        self.source.pack()
        self.trans.pack()
        self.hide_btn.pack()
