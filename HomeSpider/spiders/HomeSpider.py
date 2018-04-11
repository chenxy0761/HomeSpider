# -*- coding:utf-8 -*-
# --*-- coding:utf-8 -*-
import scrapy
from scrapy import Request, Selector
from scrapy.spiders import Spider
from selenium import webdriver
from ..items import HomespiderItem

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 巨潮资讯网--上市农业企业基本信息
class HomeSpider(Spider):
    name = 'jghq'
    start_urls = ['http://www.vegnet.com.cn/Price/List_ar310000_p1.html?marketID=0',
                  'http://www.vegnet.com.cn/Price/List_ar310000_p2.html?marketID=0',
                  'http://www.vegnet.com.cn/Price/List_ar310000_p3.html?marketID=0',
                  'http://www.vegnet.com.cn/Price/List_ar310000_p4.html?marketID=0',
                  ]

    def __init__(self):
        self.broswer = webdriver.PhantomJS()
        self.broswer.set_page_load_timeout(30)

    def parse(self, response):
        sel = Selector(response)
        body = sel.xpath('//div[@class="box"]/div/div/div[@class="pri_k"]/p').extract()
        item = HomespiderItem()
        i = 0
        while i <= len(body):
            text = sel.xpath('//div[@class="box"]/div/div/div[@class="pri_k"]/p[' + str(
                i) + ']/span[@class="k_2"]//text()').extract()
            list = []
            for ll in text:
                list.append(str(ll))
            i = i + 1
            if len(list) != 0:
                item['name'] = list[0]
                item['low_price'] = list[1]
                item['high_price'] = list[2]
                item['ave_price'] = list[3]
                item['unit'] = list[4]
            yield item
