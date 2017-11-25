from plugins.__model__ import RadioModel


class Radio(RadioModel):
    def __init__(self):
        super().__init__()
        self.name = 'Globo'

    def urls(self):
        return dict(Air='http://www.radioglobo.it/webradio-radioglobo/')

    def target(self):
        return dict(type='xpath',
                    name='(//*[@class="col-xs-12 col-sm-12 fullonaircopertina"])[2]')

    def info_to_song(self, info):
        _song = dict()
        _info = info.text.split('\n')
        _song['Artist'] = _info[4].title()
        _song['Title'] = _info[2].title()
        _song['Year'] = 'None'
        _song['Album'] = 'None'
        if 'Le Migliori' in _song['Artist']:
            _song = None
        return _song
