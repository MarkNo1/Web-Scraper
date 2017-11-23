from scraper import *
from time import sleep


class Subito:
    def __init__(self, main_url, pages=10, log_scraper=False):
        self.scraper = Scraper(log_scraper)
        self.main_url = main_url
        self.generated_urls = self.__generate_annunci_page(pages)
        self.annunci_links = []
        self.records = []

    def __generate_annunci_page(self, pages):
        annunci_urls = []
        for i in range(pages):
            url = self.main_url + '&o={}'.format(i)
            annunci_urls.append(url)
        return annunci_urls

    def purge_cookie(self):
        self.scraper.webBrowser.delete_all_cookies()

    def gathering_data(self):
        counter = 0
        tot_pages = len(self.generated_urls)
        for url in self.generated_urls:
            self.annunci_links.extend(self.get_links_from_annunci(url))
            self.purge_cookie()
            counter += 1
            print('Annunci list [{}/{}] - Scrabbered'.format(counter, tot_pages))

        counter = 0
        tot_links = len(self.annunci_links)
        for link in self.annunci_links:
            self.records.append(self.get_info_from_annuncio(link))
            self.purge_cookie()
            counter += 1
            print('Annuncio Page [{}/{}] - Scrabbered'.format(counter, tot_links))

    def get_links_from_annunci(self, url):
        # Scrabber list of annunci
        self.scraper.openUrl(url)
        target_list = [dict(type=CLASS, name='items_listing'),
                       dict(type=CLASS, name='item_list_inner')]

        annunci_list = self.scraper.get_nested_elements_from_root(target_list)

        h2 = [dict(type=TAG, name='h2')]
        href = [dict(type=LINK, name='')]

        links = []
        for annuncio in annunci_list:
            e_h2 = self.scraper.get_nested_elements(annuncio, h2)[0]
            link = self.scraper.get_nested_elements(e_h2, href)
            links.append(link)

        return links

    def get_info_from_annuncio(self, url):
        # Scrabber annuncio
        # Info
        self.scraper.openUrl(url)
        summary_class = dict(type=CLASS, name='summary')
        info = self.scraper.get_element_BY(summary_class).text.split('\n')
        # Description
        description_class = dict(type=CLASS, name='description')
        description = self.scraper.get_element_BY(description_class).text
        # Date - name
        date_name = dict(type=CLASS, name='data')
        date = self.scraper.get_element_BY(date_name).text.split('\n')[0]
        name = self.scraper.get_element_BY(date_name).text.split('\n')[1]
        # Phone
        phone_id = dict(type=ID, name='show_numb')
        phone_button = self.scraper.get_element_BY(phone_id)
        if phone_button:
            phone_button.click()
            number_id = dict(type=ID, name='adv_phone_big')
            sleep(1.5)
            number = self.scraper.get_element_BY(number_id).text
        else:
            number = 'None'

        record = dict(info=info, description=description,
                      phone=number, date=date, name=name)
        return record

    def close_browser(self):
        self.scraper.close()
