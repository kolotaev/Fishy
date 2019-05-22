import tkinter as tk

from app.front import Front


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x600')
    center(root)
    # root.after(1, lambda: root.focus_force())
    # root.focus_force()
    root.lift()
    root.attributes("-topmost", True)

    def handle_focus(event):
        if event.widget == root:
            root.focus_set()

    root.bind("<FocusIn>", handle_focus)
    Front(root).show()
    root.mainloop()
