import tkinter as tk


class Front:
    def __init__(self, parent):
        self.source = tk.Label(parent, padx=100, pady=50, text="Word!")
        self.trans = tk.Message(parent, padx=100, background='grey', pady=50, text="Translated!")

    def show(self):
        self.source.pack()
        self.trans.pack()

