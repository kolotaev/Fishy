import tkinter as tk

from ..consts import NAME, GEOMETRY
from .front import Front
from .menu import Menu
from .icons import MainIcon
from ..configurator import config


class MainFrame:
    def __init__(self):
        self.win = tk.Tk()
        self._configure()
        Front(self).add()
        Menu(self.win).add()
        MainIcon(self.win).add()

    def show(self):
        self._center()
        self._focus()

    def show_again(self):
        self.win.update()
        self.win.deiconify()
        self.show()

    def hide(self):
        self.win.overrideredirect(1)
        self.win.withdraw()

    def destroy(self):
        self.win.destroy()

    @property
    def is_alive(self):
        return self.win.winfo_exists()

    def _configure(self):
        self.win.title(NAME)
        if config.getboolean('window', 'resizable'):
            self.win.resizable(0, 0)
        self.win.geometry(GEOMETRY)

    def _center(self):
        self.win.update_idletasks()
        width = self.win.winfo_width()
        height = self.win.winfo_height()
        x = (self.win.winfo_screenwidth() // 2) - (width // 2)
        y = (self.win.winfo_screenheight() // 2) - (height // 2)
        self.win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def _focus(self):
        self.win.lift()
        self.win.attributes("-topmost", True)
        self.win.bind("<FocusIn>", lambda event: self.win.focus_set() if event.widget == self.win else 0)
