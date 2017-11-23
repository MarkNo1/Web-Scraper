from plugins.__plugins__ import PluginRadio
from scraper.scraper import Scraper
from time import sleep

plug = PluginRadio()
plug.load_plugins()
scrap = Scraper()


while(1):
    for plugin in plug.plugins:
        radio = plugin.Radio()
        print(radio.name())
        for station, url in radio.urls().items():
            print(station)
            scrap.openUrl(url)
            info = scrap.get_element_BY(radio.target())
            song = radio.info_to_song(info)
            print(song)
    sleep(5)
