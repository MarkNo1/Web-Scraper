from mark_utils.scraper import Scraper
from selenium.webdriver.support.ui import Select
from time import sleep
from mark_utils.color import Color as c
from mark_utils.text import between
from tqdm import tqdm

LOG = True
HEADLESS = True
TOR = True


class Target:
    class Search:
        name = dict(ID='searchtext')
        category = dict(ID='cat')
        area = dict(ID='searcharea')
        button_continue = dict(CLASS='btnGreen')

    class ListAd:
        list_link_element = [dict(CLASS='items_listing'), dict(CLASS='item_list_inner')]
        raw_link = dict(TAG='h2')
        link = dict(LINK='')
        button_next = dict(CLASS='pagination_next')
        number_page = dict(CLASS='number_container')

    class Ad:
        summary = dict(CLASS='summary')
        description = dict(CLASS='description')
        date_name = dict(CLASS='data')
        phone_button = dict(ID='show_numb')
        phone_number = dict(ID='adv_phone_big')


class Page:
    scraper = Scraper(log=LOG, headless=HEADLESS, tor=TOR)
    I = c.blue('Page/')

    class Search:
        I = c.orange('Search/')

        def goto_url(self):
            D = c.green('@goto_url')
            url = 'https://www.subito.it'
            Page.scraper.openUrl(url)
            print(Page.I + self.I + D, c.underline(url))

        def what(self, text=None):
            D = c.green('@what')
            if text is None:
                text = input('What you want search ->  ')
            search = Page.scraper.get_element_BY(Target.Search.name)
            search.send_keys(text)
            print(Page.I + self.I + D, c.underline(text))

        def catagory(self, idx=None):
            D = c.green('@catagory')
            category = Page.scraper.get_element_BY(Target.Search.category)
            view = Select(category)
            options = view.options
            print(c.underline('Category:'))
            for i, op in enumerate(options):
                print('[{}] - {}'.format(c.orange(str(i)), c.blue(op.text)))
            if idx is None:
                idx = int(input('\nInsert number [i] -> '))
            chs = options[idx].text
            options[idx].click()
            print(Page.I + self.I + D, c.underline(chs))

        def area(self, idx=None):
            D = c.green('@area')
            area = Page.scraper.get_element_BY(Target.Search.area)
            view = Select(area)
            options = view.options
            print(c.underline('Geographic Area:'))
            for i, op in enumerate(options):
                print('[{}] - {}'.format(c.orange(str(i)), c.blue(op.text)))
            if idx is None:
                idx = int(input('insert the number [i] -> '))
            chs = options[idx].text
            options[idx].click()
            print(Page.I + self.I + D, c.underline(chs))

        def continue_button(self):
            D = c.green('@continue_button')
            b_continue = Page.scraper.get_element_BY(Target.Search.button_continue)
            b_continue.click()
            print(Page.I + self.I + D, c.underline('Continue'))

    class ListAd:
        I = c.orange('ListAd/')

        def links(self):
            D = c.green('@links')
            links = []
            raw_ads = Page.scraper.get_nested_elements_from_root(
                Target.ListAd.list_link_element)
            for raw_ad in raw_ads:
                raw_link = Page.scraper.find_elements_BY(raw_ad, Target.ListAd.raw_link)
                link = Page.scraper.find_elements_BY(raw_link[0], Target.ListAd.link)
                links.append(link)
            print(Page.I + self.I + D, 'Founded links: ', c.underline(str(len(links))))
            return links

        def next(self, check=False):
            D = c.green('@next')
            next_b = Page.scraper.get_element_BY(Target.ListAd.button_next)
            link = Page.scraper.find_elements_BY(next_b, Target.ListAd.link)
            if link:
                if check:
                    return True

                Page.scraper.openUrl(link)
                print(Page.I + self.I + D, c.underline('Next'))
                return True
            print(Page.I + self.I + D, c.red('Finish'))
            return False

        def index_page(self):
            idx = Page.scraper.get_element_BY(
                Target.ListAd.number_page).get_attribute('innerHTML')
            idx = between('<strong>', '</strong>', idx)
            return idx

        def pages_links(self, chs=None):

            if chs is None:
                chs = input('How many page you want scrab? type: int or "all" \n')

            if chs == 'all':
                chs = 10000
            else:
                try:
                    chs = int(chs)
                except ValueError:
                    print('type: int or "all"')

            links = dict()
            for i in tqdm(range(chs), desc='Pages: '):
                idx = self.index_page()
                links[idx] = self.links()
                if self.next() is False:
                    break
            return links

    class Ad:
        I = c.orange('Ad/')

        def record(self, url, page_idx):
            record = dict()
            record['page_index'] = page_idx
            record['url'] = url
            Page.scraper.openUrl(url)
            # General Info
            record['info'] = Page.scraper.get_element_BY(
                Target.Ad.summary).text.split('\n')
            # Description
            record['description'] = Page.scraper.get_element_BY(
                Target.Ad.description).text
            # Date - name
            record['date'] = Page.scraper.get_element_BY(
                Target.Ad.date_name).text.split('\n')[0]
            record['name'] = Page.scraper.get_element_BY(
                Target.Ad.date_name).text.split('\n')[1]
            # Phone
            phone_button = Page.scraper.get_element_BY(Target.Ad.phone_button)
            if phone_button:
                Page.scraper.webBrowser.execute_script(
                    "arguments[0].click();", phone_button)
                sleep(1)
                number_id = dict(ID='adv_phone_big')
                record['phone'] = Page.scraper.get_element_BY(Target.Ad.phone_number).text
            else:
                record['phone'] = 'None'

            return record

        def records_from_ad_links(self, ad_links):
            temp_db = []
            for page, list_link in tqdm(ad_links.items(), desc='Pages: '):
                for url in tqdm(list_link, desc='Links: '):
                    try:
                        temp_db.append(self.record(url, page))
                    except Exception as e:
                        pass

            return temp_db
