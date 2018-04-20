# -*- coding:utf-8 -*-
# --*-- coding:utf-8 -*-
import scrapy
import time
from scrapy import Selector
from scrapy.spiders import Spider
import sys
from ..items import MoviespiderItem

reload(sys)
sys.setdefaultencoding('utf-8')


class MovieSpider(Spider):
    name = 'movie'
    start_urls = ['https://movie.douban.com/',
                  ]

    def parse(self, response):
        sel = Selector(response)
        body = sel.xpath('//div[@id="screening"]//li[@class="title"]/a/@href').extract()
        for url in body:
            time.sleep(2)
            yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        sell = Selector(response)
        sites = sell.xpath('//div[@id="info"]').extract()[0]
        title = sell.xpath('//div[@id="content"]/h1/span[1]//text()').extract()[0]
        while '<' in sites:
            sites = sites.replace(sites[sites.index('<'):sites.index('>') + 1], "")
        site = sites.replace(" ", "")
        print(title.split())
        item = MoviespiderItem()
        item['movie'] = title.strip()
        item['country'] = ""
        item['performer'] = ""
        for list in site.split('\n'):
            map = list.split(':')
            if map[0] == '导演':
                item['director'] = map[1]
            if map[0] == '主演':
                item['performer'] = map[1]
            if map[0] == '类型':
                item['type'] = map[1]
            if map[0] == '制片国家/地区':
                item['country'] = map[1]
            if map[0] == '语言':
                item['language'] = map[1]
            if map[0] == '上映日期':
                item['show'] = map[1]
            if map[0] == '片长':
                item['length'] = map[1]
        yield item
