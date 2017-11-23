from plugins.__model__ import RadioModel


class Radio(RadioModel):
    def urls(self):
        return dict(Air='http://www.radioglobo.it/webradio-radioglobo/')

    def target(self):
        return dict(type='xpath',
                    name='(//*[@class="col-xs-12 col-sm-12 fullonaircopertina"])[2]')

    def info_to_song(self, info):
        _song = None
        if info is not None:
            _song = info.text.split('\n')
        return _song

    def name(self):
        return 'Globo'
