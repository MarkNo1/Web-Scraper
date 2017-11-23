from plugins.__model__ import RadioModel
import re


def clean_text(text):
    cl = re.compile('[,\.:!?/]')
    return cl.sub("", text.title())


class Radio(RadioModel):
    def urls(self):
        return dict(
            UrbanNight="http://www.r101.it/radio/popup-diretta.shtml?asc=urban-night",
            Air="http://www.r101.it/radio/popup-diretta.shtml?asc=onair-sito",
            Enjoy="http://www.r101.it/radio/popup-diretta.shtml?asc=enjoy"
        )

    def target(self):
        return dict(type='class', name='playonair')

    def info_to_song(self, info):
        _song = None
        if info is not None:
            info = info.text.split('\n')
            T, Ar, Al, An = 'Titolo', 'Artista', 'Album', 'Anno'
            _song = None
            if len(info) > 3:
                _song = dict()
                if info[1].partition(T)[1] is T:
                    titolo = info[1].partition(T + ':')[2]
                    _song[T] = clean_text(titolo)

                if info[0].partition(Ar)[1] is Ar:
                    artista = info[0].partition(Ar + ':')[2]
                    _song[Ar] = clean_text(artista)

                if info[3].partition(Al)[1] is Al:
                    album = info[3].partition(Al + ':')[2]
                    _song[Al] = clean_text(album)

                if info[2].partition(An)[1] is An:
                    anno = info[2].partition(An + ':')[2]
                    _song[An] = clean_text(anno)
        return _song

    def name(self):
        return 'R101'
