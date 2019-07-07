import tkinter as tk

from ..consts import NAME, MODAL_NAME


class ModalBox:
    def __init__(self, main):
        self.main = main
        self.dialog = None
        self.label = None
        self.button = None
        self.title = NAME + ' - ' + MODAL_NAME

    def show(self):
        self.dialog = tk.Toplevel()
        self.dialog.title(self.title)
        self.label = tk.Label(self.dialog, text='Do you want to enable my \n\n parent window again?')
        self.button = tk.Button(self.dialog, text='Close', width=10, command=self.close)
        # THE CLUE
        # self.win.wm_attributes("-disabled", True)

        # Tell the window manager, this is the child widget.
        # Interesting, if you want to let the child window
        # flash if user clicks onto parent
        # self.dialog.transient(self)

        self.label.pack(side=tk.TOP)
        self.button.pack(expand=False)

        # self.main.win.update_idletasks()
        dimensions = map(lambda x: x - 10, self.main.get_dimensions())
        self.dialog.geometry('{}x{}+{}+{}'.format(*dimensions))

        # Bring this window to the top
        self.main.win.attributes('-topmost', False)
        self.dialog.attributes('-topmost', True)

        # This is watching the window manager close button
        # and uses the same callback function as the other buttons
        # (you can use which ever you want, BUT REMEMBER TO ENABLE
        # THE PARENT WINDOW AGAIN)
        self.dialog.protocol('WM_DELETE_WINDOW', self.close)

    def close(self):
        # self.win.wm_attributes("-disabled", False) # IMPORTANT!
        self.dialog.destroy()
        self.main.win.attributes('-topmost', True)
        # Possibly not needed, used to focus parent window again
        self.main.win.deiconify()
