from abc import ABCMeta


class SpeechProvider(metaclass=ABCMeta):
    def speak(self, text, lang, **kwargs):
        pass


class GoogleTTS(SpeechProvider):
    def __init__(self):
        try:
            from google_speech import Speech
            self.speech = Speech
        except ImportError:
            print('Please install "sox" to use Google TTS')
            exit(1)

    def speak(self, text, lang, **kwargs):
        self.speech(text, lang).play()
