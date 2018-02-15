from plugins.__model__ import RadioModel
import re


class Radio(RadioModel):
    def __init__(self):
        super().__init__()
        self.name = 'Virgin'

    def urls(self):
        return dict(
            Air='http://www.virginradio.it/sezioni/1184/virgin-radio-on-air',
            HardRock='http://www.virginradio.it/sezioni/1218/virgin-radio-hard-rock',
            RockHits='http://www.virginradio.it/sezioni/1239/virgin-radio-rock-hits'
        )

    def target(self):
        return dict(CLASS='textual')

    def info_to_song(self, info):
        _song = None
        song_record = None
        if info is not None:
            info = info.text.split('\n')
            cleaner = re.compile('[,\.!?/]')
            _song = []
            space = " "
            for i in range(len(info)):
                if info[i] not in {'TITOLO:', 'ARTISTA:', 'ALBUM:', 'ANNO:'}:
                    _song.append(cleaner.sub(
                        "", space.join(info[i].split()).title()))
            if len(_song) is 4:
                song_record = dict(
                    Title=_song[0], Artist=_song[1], Album=_song[2], Year=_song[3])

        return song_record
