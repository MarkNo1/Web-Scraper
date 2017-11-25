from plugins.__model__ import RadioModel
from time import sleep
import re


def clean_text(text):
    cl = re.compile('[,\.:!?/]')
    return cl.sub("", text.title())


class Radio(RadioModel):
    def __init__(self):
        super().__init__()
        self.name = 'Rds'

    def urls(self):
        return dict(Air='http://www.rds.it/diretta/')

    def target(self):
        return dict(type='class',
                    name='brano_info_player_text')

    def info_to_song(self, info):
        _song = None
        info = info.text.split('\n')
        if len(info) > 1:
            if 'UNDEFINED' in info[0]:
                _song = None
            else:
                _song = dict(
                    Title=info[1].title(), Artist=info[0].title(), Album=None, Year=None)

        return _song
