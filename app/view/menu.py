import tkinter as tk
import platform


class Menu:
    def __init__(self, root):
        self.pw = root
        menubar = tk.Menu(self.pw)
        if platform.system() == 'Darwin':
            appmenu = tk.Menu(menubar, name='apple')
            menubar.add_cascade(menu=appmenu)
            appmenu.add_command(label='About My Application')
            appmenu.add_separator()
            self.pw.createcommand('tk::mac::ShowPreferences', lambda: print('Not yet implemented'))
        window_menu = tk.Menu(menubar, name='window')
        menubar.add_cascade(menu=window_menu, label='Window')
        self.menubar = menubar

    def add(self):
        self.pw['menu'] = self.menubar
        # Expose to the main view
        self.pw.menubar = self.menubar
