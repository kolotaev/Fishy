import tkinter as tk
import threading

from .consts import NAME, GEOMETRY, SHOW_TIMEOUT, RESIZABLE
from .front import Front
from .menu import Menu
from .icons import MainIcon


class Application:
    def __init__(self):
        self.win = tk.Tk()

        self._configure()

        Front(self).add()
        Menu(self.win).add()
        MainIcon(self.win).add()

        self.show()
        self.showing_thread = ShowingThread(self)
        self.showing_thread.start()

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

    def start(self):
        self.win.mainloop()

    def _configure(self):
        self.win.protocol("WM_DELETE_WINDOW", self._destroy)
        self.win.title(NAME)
        self.win.resizable(0, 0) if RESIZABLE else None
        self.win.geometry(GEOMETRY)

    def _destroy(self):
        print('killing...')
        self.showing_thread.terminate()
        self.win.destroy()

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


class ShowingThread(threading.Thread):
    def __init__(self, win):
        self.win = win
        self._running_flag = False
        self.stop = threading.Event()
        super().__init__()

    def run(self):
        try:
            while not self.stop.wait(1):
                self._running_flag = True
                print("Waiting for %d secs..." % SHOW_TIMEOUT)
                self.win.show_again()
                self.stop.wait(SHOW_TIMEOUT)
        finally:
            self._running_flag = False

    def terminate(self):
        self.stop.set()
