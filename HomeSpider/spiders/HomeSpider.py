# -*- coding:utf-8 -*-
import selenium as selenium
from scrapy import Selector
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class HomeSpider(CrawlSpider):
    name = 'home'
    allowed_domains = ['cnbeta.com']
    start_urls = ['http://www.jb51.net']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(SgmlLinkExtractor(allow=('/articles/.*\.htm', )),
             callback='parse_page', follow=True),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
    )

    def __init__(self):
        CrawlSpider.__init__(self)
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*firefox", "http://www.jb51.net")
        self.selenium.start()

    def __del__(self):
        self.selenium.stop()
        print self.verificationErrors
        CrawlSpider.__del__(self)


    def parse_page(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        sel = Selector(response)

        sel = self.selenium
        sel.open(response.url)
        sel.wait_for_page_to_load("30000")
        import time

        time.sleep(2.5)