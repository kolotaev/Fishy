import configparser
from os.path import expanduser, exists, join

from .consts import CONF_FILE_NAME


__all__ = [
    'init',
    'config',
    'get_show_timeout',
]

DEFAULTS = {
    'window': {
        'resizable': 'yes',
    },
    'popup': {
        'show_timeout_value': 2,
        'show_timeout_unit': 'sec',
    },
    'corpus': {
        'current': 1,
        'repeat_count': 30,
    }
}

CONFIG_PATH = join(expanduser('~'), CONF_FILE_NAME)
config = configparser.ConfigParser()


def init():
    create_if_missing()
    read()


def create_if_missing():
    if not exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'w') as configfile:
            default_config = configparser.ConfigParser()
            default_config['window'] = DEFAULTS['window']
            default_config['popup'] = DEFAULTS['popup']
            default_config['corpus'] = DEFAULTS['corpus']
            default_config.write(configfile)


def read():
    global config
    config.read(CONFIG_PATH)


def get_show_timeout():
    timeout_unit = config.get('popup', 'show_timeout_unit')
    if timeout_unit == 'hour':
        unit = 60 * 60
    elif timeout_unit == 'min':
        unit = 60
    else:
        unit = 1
    return config.getint('popup', 'show_timeout_value') * unit
