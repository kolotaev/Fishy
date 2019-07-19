import tkinter as tk

from ..consts import NAME, MODAL_NAME


class ModalBox:
    def __init__(self, main, config):
        self.main = main
        self.dialog = None
        self.label = None
        self.button = None
        self.config = config
        self.title = NAME + ' - ' + MODAL_NAME

    def show(self, text, translation):
        text_all = self._format_text(text, translation)
        self.dialog = tk.Toplevel()
        self.dialog.title(self.title)

        font = (self.config.get('window', 'modal-font-family'), self.config.get('window', 'modal-font-size'))
        self.label = tk.Text(self.dialog, font=font, padx=2, pady=2, wrap=tk.WORD)
        self.label.config(state=tk.NORMAL)
        self.label.insert(tk.END, text_all)
        self.label.config(state=tk.DISABLED)

        self.button = tk.Button(self.dialog, text='Close', width=10, command=self.close)

        # pack elements
        self.button.pack(expand=False)
        self.label.pack(padx=16, pady=4, ipadx=4, ipady=10)

        # self.main.win.update_idletasks()
        self.dialog.geometry('{}x{}+{}+{}'.format(*self.main.get_dimensions()))

        # Bring this window to the top
        self.main.win.attributes('-topmost', False)
        self.dialog.attributes('-topmost', True)

        self.dialog.protocol('WM_DELETE_WINDOW', self.close)

    def close(self):
        self.dialog.destroy()
        self.main.win.attributes('-topmost', True)

    @staticmethod
    def _format_text(text, translation):
        tr = ''
        if isinstance(translation, str):
            tr = translation
        elif isinstance(translation, (list, tuple)):
            for part in translation:
                tr += part[0] + ':\n'
                for trans, synonyms in part[2]:
                    tr += '  %s - %s\n\n' % (trans, ', '.join(synonyms))
        return "%s\n------\n%s\n" % (text, tr)
