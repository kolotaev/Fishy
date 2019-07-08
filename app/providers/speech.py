from abc import ABCMeta, abstractmethod


def create_speech_provider(config):
    # currently we have only one provider
    return GoogleTTS(config)


class SpeechProvider(metaclass=ABCMeta):
    def __init__(self, config):
        self.language = config.get('corpus', 'language')

    @abstractmethod
    def speak(self, text, lang, **kwargs):
        pass


class GoogleTTS(SpeechProvider):
    def __init__(self, config):
        super().__init__(config)
        try:
            from google_speech import Speech
            self.speech = Speech
        except ImportError:
            print('Please install "sox" to use Google TTS')
            exit(1)

    def speak(self, text, lang=None, **kwargs):
        if not lang:
            lang = self.language
        self.speech(text, lang).play()
