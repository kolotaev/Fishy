from app.front import Front
from app.root import Root


if __name__ == '__main__':
    root = Root()
    Front(root).show()
    root.start()
