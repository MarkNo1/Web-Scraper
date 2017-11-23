from plugins.__model__ import RadioModel
import re


class Radio(RadioModel):
    def urls(self):
        return dict(
            Air='http://www.virginradio.it/sezioni/1184/virgin-radio-on-air',
            HardRock='http://www.virginradio.it/sezioni/1218/virgin-radio-hard-rock',
            RockHits='http://www.virginradio.it/sezioni/1239/virgin-radio-rock-hits'
        )

    def target(self):
        return dict(type='class', name='textual')

    def info_to_song(self, info):
        _song = None
        if info is not None:
            info = info.text.split('\n')
            cleaner = re.compile('[,\.!?/]')
            _song = []
            space = " "
            for i in range(len(info)):
                if info[i] not in {'TITOLO:', 'ARTISTA:', 'ALBUM:', 'ANNO:'}:
                    _song.append(cleaner.sub("", space.join(info[i].split()).title()))
            song_record = dict()

        return _song

    def name(self):
        return 'Virgin'
