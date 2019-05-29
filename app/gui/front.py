import tkinter as tk

from ..conf import config


class Front:
    def __init__(self, app):
        self.app = app
        self.pw = app.win
        self.conf = config

    def add(self):
        tk.Label(self.pw, padx=100, pady=50, text="Юникод!").pack()
        tk.Message(self.pw, padx=100, background='grey', pady=50, text="Translated!").pack()
        tk.Button(self.pw, text='Hide', command=self.app.hide).pack()
        tk.Message(self.pw, padx=100, background='grey', pady=50,
                   text=str(self.conf.getboolean('window', 'resizable'))).pack()
