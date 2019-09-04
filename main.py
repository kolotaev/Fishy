import sys

from app import Application


def run():
    if len(sys.argv) > 0:
        config = sys.argv[1]
    else:
        config = None
    Application.launch(config)


if __name__ == '__main__':
    run()
