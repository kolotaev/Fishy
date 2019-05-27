import tkinter as tk


class Menu:
    def __init__(self, app):
        self.pw = app.win
        menubar = tk.Menu(self.pw)
        appmenu = tk.Menu(menubar, name='apple')
        menubar.add_cascade(menu=appmenu)
        appmenu.add_command(label='About My Application')
        appmenu.add_separator()
        window_menu = tk.Menu(menubar, name='window')
        menubar.add_cascade(menu=window_menu, label='Window')
        self.pw.createcommand('tk::mac::ShowPreferences', lambda: print('00'))
        self.menubar = menubar

    def add(self):
        self.pw['menu'] = self.menubar
