from plugins.__model__ import RadioModel
import re


def clean_text(text):
    cl = re.compile('[,\.:!?/]')
    return cl.sub("", text.title())


class Radio(RadioModel):
    def __init__(self):
        super().__init__()
        self.name = '105'

    def urls(self):
        return dict(Air='http://www.105.net/sezioni/733/radio-105-diretta')

    def target(self):
        return dict(type='class',
                    name='textual')

    def info_to_song(self, info):
        _song = None
        info = info.text.split('\n')
        if len(info) > 1:
            _song = dict(
                Title=info[1].title(), Artist=info[0].title(), Album=None, Year=None)

        return _song
