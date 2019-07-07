import tkinter as tk

from ..consts import NAME, MODAL_NAME


class ModalBox:
    def __init__(self, main):
        self.main = main
        self.dialog = None
        self.label = None
        self.button = None
        self.title = NAME + ' - ' + MODAL_NAME

    def show(self, text, translation):
        text_all = text + "\n ------ \n" + translation + "\n"
        self.dialog = tk.Toplevel()
        self.dialog.title(self.title)
        self.label = tk.Label(self.dialog, text=text_all)
        self.button = tk.Button(self.dialog, text='Close', width=10, command=self.close)

        self.label.pack(side=tk.TOP)
        self.button.pack(expand=False)

        # self.main.win.update_idletasks()
        self.dialog.geometry('{}x{}+{}+{}'.format(*self.main.get_dimensions()))

        # Bring this window to the top
        self.main.win.attributes('-topmost', False)
        self.dialog.attributes('-topmost', True)

        self.dialog.protocol('WM_DELETE_WINDOW', self.close)

    def close(self):
        self.dialog.destroy()
        self.main.win.attributes('-topmost', True)
