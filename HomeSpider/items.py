# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HomespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    low_price = scrapy.Field()
    high_price = scrapy.Field()
    ave_price = scrapy.Field()
    unit = scrapy.Field()
    date = scrapy.Field()


class MoviespiderItem(scrapy.Item):
    movie = scrapy.Field()
    type = scrapy.Field()
    length = scrapy.Field()
    performer = scrapy.Field()
    country = scrapy.Field()
    director = scrapy.Field()
    show = scrapy.Field()
    language = scrapy.Field()


