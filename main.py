from app.gui import Application
import app.conf


if __name__ == '__main__':
    app.conf.init()
    Application().start()
