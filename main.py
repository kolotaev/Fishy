from app.front import Front
from app.root import Root


if __name__ == '__main__':
    root = Root().get
    Front(root).show()
    root.mainloop()
