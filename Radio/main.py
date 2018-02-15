from mark_utils.scraper import Scraper
from mark_utils.color import Color as c
from plugins.__plugins__ import PluginRadio
from time import sleep, ctime
import time
from tabulate import tabulate
import sys


class Nice_print:
    @staticmethod
    def radio(radio):
        sys.stdout.write(('\n\n|Radio: {} '.format(c.blue(radio.name))))

    @staticmethod
    def station(station):
        sys.stdout.write('\n|Station: {} '.format(c.orange(station)))

    @staticmethod
    def song(song):
        if song:
            artist = c.purple(str(song['Artist']))
            title = c.purple(str(song['Title']))
            album = c.purple(str(song['Album']))
            year = c.purple(str(song['Year']))
            sys.stdout.write(
                '\n|{}: - Artist: {}, Title: {}, Album: {}, Year: {}.'.format(c.pink(time.strftime("%X")), artist, title, album, year))


class Programm():
    def __init__(self):
        self.started = ctime()
        self.scrap = Scraper(log=False, headless=True)
        self.plug = PluginRadio()
        self.plug.load_plugins()

    def one_radio(self, plug_station):
        radio = plug_station.Radio()
        Nice_print.radio(radio)
        for station, url in radio.urls().items():
            Nice_print.station(station)
            song = self.one_station(radio, url)
            Nice_print.song(song)

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
