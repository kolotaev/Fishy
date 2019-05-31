from app.view import Application
import app.configurator


if __name__ == '__main__':
    app.configurator.init()
    Application().start()
