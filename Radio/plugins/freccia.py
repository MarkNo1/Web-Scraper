from plugins.__model__ import RadioModel
from time import sleep


class Radio(RadioModel):
    def __init__(self):
        super().__init__()
        self.name = 'Freccia'

    def urls(self):
        return dict(Air='http://www.radiofreccia.it/fm/')

    def target(self):
        target_list = [dict(XPATH='(//*[@class="white first-line"])[1]'),
                       dict(XPATH='(//*[@class="white second-line"])[1]'),
                       dict(XPATH='(//*[@class="gray third-line"])[1]')]
        sleep(4)
        return target_list

    def info_to_song(self, info_list):
        _song = []
        for info in info_list:
            if info is not None:
                _song.append(info.text)
        song_record = dict(
            Title=_song[1], Artist=_song[0], Album=_song[2], Year='None')
        if song_record['Title'] is '':
            song_record = None
        elif 'Seconda riga' in song_record['Title']:
            song_record = None
        return song_record
