from skeleton import *
from mark_utils.color import Color as c


class Subito:
    ad_links = None
    db = None

    def __init__(self):
        self.search = Page().Search()
        self.listad = Page().ListAd()
        self.ad = Page().Ad()

    def searchPage(self, what=None, category=None, area=None):
        self.search.goto_url()
        self.search.what(what)
        self.search.catagory(category)
        self.search.area(area)
        self.search.continue_button()

    def listAdPage(self, n_page):
        try:
            self.ad_links = self.listad.pages_links(n_page)
        except Exception as e:
            print(c.red(e))

    def create_db(self):
        if self.ad_links:
            self.db = self.ad.records_from_ad_links(self.ad_links)
