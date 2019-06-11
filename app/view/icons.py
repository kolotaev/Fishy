import platform

from ..consts import ICON_PATH


class MainIcon:
    def __init__(self, root):
        self.root = root

    def add(self):
        system = platform.system()
        try:
            if system == 'Darwin':
                self.root.wm_iconbitmap(ICON_PATH)
        except Exception as e:
            print(e)
