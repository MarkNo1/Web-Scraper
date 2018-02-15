from plugins.__model__ import RadioModel
import re


def clean_text(text):
    cl = re.compile('[,\.:!?/]')
    return cl.sub("", text.title())


class Radio(RadioModel):
    def __init__(self):
        super().__init__()
        self.name = 'R101'

    def urls(self):
        return dict(
            UrbanNight="http://www.r101.it/radio/popup-diretta.shtml?asc=urban-night",
            Air="http://www.r101.it/radio/popup-diretta.shtml?asc=onair-sito",
            Enjoy="http://www.r101.it/radio/popup-diretta.shtml?asc=enjoy"
        )

    def target(self):
        return dict(CLASS='playonair')

    def info_to_song(self, info):
        _song = None
        if info is not None:
            info = info.text.split('\n')
            T, Ar, Al, An = 'Titolo', 'Artista', 'Album', 'Anno'
            if len(info) > 3:
                _song = dict()
                if info[1].partition(T)[1] is T:
                    titolo = info[1].partition(T + ':')[2]
                    _song['Title'] = clean_text(titolo)

                if info[0].partition(Ar)[1] is Ar:
                    artista = info[0].partition(Ar + ':')[2]
                    _song['Artist'] = clean_text(artista)

                if info[3].partition(Al)[1] is Al:
                    album = info[3].partition(Al + ':')[2]
                    _song['Album'] = clean_text(album)

                if info[2].partition(An)[1] is An:
                    anno = info[2].partition(An + ':')[2]
                    year = clean_text(anno)
                    if ' 0' in year:
                        _song['Year'] = 'None'
                    else:
                        _song['Year'] = year
        return _song
