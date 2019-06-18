from configparser import ConfigParser
from os.path import exists


__all__ = [
    'Config',
]

DEFAULTS = {
    'window': {
        'initial-size': '800x600',
        'resizable': 'yes',
        'word-font-family': 'Courier',
        'word-font-size': 22,
        'explain-font-family': 'Courier',
        'explain-font-size': 16,
    },
    'popup': {
        'type': 'clock',
        'show_timeout_value': 2,
        'show_timeout_unit': 'sec',
        'start_time': '13.00',
        'end_time': '22.00',
    },
    'corpus': {
        'file_path': 'words.csv'
    },
    'learn': {
        'current': 1,
        'words-per-day': 30,
        'words-repeat': 30,
    }
}


class Config(ConfigParser):
    def __init__(self, path, create=False, **kwargs):
        self.path = path
        self.create = create
        super().__init__(**kwargs)

    def init(self):
        if self.create:
            self.create_if_missing()
        self.read(self.path)

    def create_if_missing(self):
        if not exists(self.path):
            with open(self.path, 'w') as configfile:
                default_config = ConfigParser()
                default_config['window'] = DEFAULTS['window']
                default_config['popup'] = DEFAULTS['popup']
                default_config['corpus'] = DEFAULTS['corpus']
                default_config['learn'] = DEFAULTS['learn']
                default_config.write(configfile)
        else:
            print('file already exists')

    def get_show_timeout(self):
        timeout_unit = self.get('popup', 'show_timeout_unit')
        if timeout_unit == 'hour':
            unit = 60 * 60
        elif timeout_unit == 'min':
            unit = 60
        else:
            unit = 1
        return self.getint('popup', 'show_timeout_value') * unit

    def save(self, section, option, value):
        self.set(section, option, str(value))
        with open(self.path, 'w') as configfile:
            self.write(configfile)
