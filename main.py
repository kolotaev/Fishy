from app.view import Application
import app.configurator


def run():
    app.configurator.init()
    Application().start()


if __name__ == '__main__':
    run()
