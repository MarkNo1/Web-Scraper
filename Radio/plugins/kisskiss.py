from plugins.__model__ import RadioModel
from time import sleep
import re


def clean_text(text):
    cl = re.compile('[,\.:!?/]')
    return cl.sub("", text.title())


class Radio(RadioModel):
    def __init__(self):
        super().__init__()
        self.name = 'KissKiss'

    def urls(self):
        return dict(Air='http://www.kisskiss.it/player/')

    def target(self):
        sleep(2)
        return dict(CLASS='info')

    def info_to_song(self, info):
        _song = None
        info = info.text.split('\n')
        T, Ar, Al = 'TITOLO', 'ARTISTA', 'ALBUM'
        if len(info) > 2:
            _song = dict()
            if info[0].partition(T)[1] is T:
                titolo = info[0].partition(T + ':')[2]
                _song['Title'] = clean_text(titolo)

            if info[1].partition(Ar)[1] is Ar:
                artista = info[1].partition(Ar + ':')[2]
                _song['Artist'] = clean_text(artista)

            if info[2].partition(Al)[1] is Al:
                album = info[2].partition(Al + ':')[2]
                _song['Album'] = clean_text(album)
            _song['Year'] = None

        return _song
