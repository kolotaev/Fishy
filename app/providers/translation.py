from abc import ABCMeta, abstractmethod

from googletrans import Translator


def create_translation_provider(config):
    # currently we have only one provider
    return GoogleTranslate(config)


class TranslateProvider(metaclass=ABCMeta):
    def __init__(self, config):
        self.from_language = config.get('corpus', 'language')
        self.to_language = config.get('corpus', 'additional-translate-to-lang')

    @abstractmethod
    def translate(self, text, from_lang, to_lang, **kwargs):
        pass


class GoogleTranslate(TranslateProvider):
    def __init__(self, config):
        super().__init__(config)
        self.translator = Translator()

    def translate(self, text, from_lang=None, to_lang=None, **kwargs):
        if not from_lang:
            from_lang = self.from_language
        if not to_lang:
            to_lang = self.to_language
        tt = self.translator.translate(text, src=from_lang, dest=to_lang)
        return tt.text
