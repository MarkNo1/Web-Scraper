from plugins.__plugins__ import PluginRadio
from scraper.scraper import Scraper
from time import sleep, ctime


class Programm():
    def __init__(self):
        self.started = ctime()
        self.scrap = Scraper()
        self.plug = PluginRadio()
        self.plug.load_plugins()

    def one_radio(self, plug_station):
        radio = plug_station.Radio()
        for station, url in radio.urls().items():
            song = self.one_station(radio, url)
            print('\nRadio: {}\nstation: {}\nSong: {}'.format(
                radio.name, station, song))

    def one_station(self, radio, url):
        self.scrap.openUrl(url)
        info = self.scrap.get_element_BY(radio.target())
        song = radio.info_to_song(info)
        return song

    def one_cicle(self):
        self.plug.reload_plugins()
        for radio_plug in self.plug.plugins:
            self.one_radio(radio_plug)

    def run(self):
        while(1):
            try:
                self.one_cicle()

            except Exception as e:
                print('Error ---> {}'.format(e))


main = Programm()
# main.run()
