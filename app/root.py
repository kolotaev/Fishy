import tkinter as tk
import time
import threading


class Root:
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry('800x600')
        self.show()
        self.hide_thread = self._start_hiding()

    @property
    def get(self):
        return self.win

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
        self.win.bind("<FocusIn>", lambda event: self.win.focus_set() if event.widget == self.win else None)

    def _start_hiding(self):
        def show_window(win):
            while True:
                print("Waiting for 5 secs...")
                time.sleep(5)
                win.show_again()
        thr = threading.Timer(5, function=show_window, args=[self])
        thr.start()
        return thr

    def show(self):
        self._center()
        self._focus()

    def show_again(self):
        self.win.deiconify()
        self.show()

    def hide(self):
        self.win.overrideredirect(1)
        self.win.withdraw()
