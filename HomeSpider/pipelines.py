# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import datetime

from HomeSpider.items import HomespiderItem, MoviespiderItem
from util.con_MySQL import Dba

logger = logging.getLogger(__name__)


class HomespiderPipeline(object):
    def __init__(self):

        self.ora = Dba()
        self.CaiJia_Sql = """
                INSERT INTO HOME_CAIJIA(name, low_price, high_price, ave_price,unit,date) 
                values('%s', '%s', '%s', '%s', '%s', now())
            """
        self.Movie_Sql = """
                INSERT INTO HOME_MOVIE(movie,type,length,performer, country, director, `show`,`language`,`score`) 
                values('%s', '%s', '%s', '%s', '%s', '%s','%s','%s','%s')
            """

    # pipeline默认调用
    def process_item(self, item, spider):
        if isinstance(item, HomespiderItem):
            now = datetime.datetime.now()
            date = now.strftime('%Y-%m-%d')
            sql = self.CaiJia_Sql % (
                item['name'],
                item['low_price'],
                item['high_price'],
                item['ave_price'],
                item['unit']
            )
            try:
                self.ora.cux_sql(self.ora.connect(), sql, item['name'], date)
                # cursor.execute(sql, (name, low_price, high_price, ave_price, unit))
                # conn.commit()
            except Exception as e:
                print(e)
        if isinstance(item, MoviespiderItem):
            sql = self.Movie_Sql % (
                item['movie'],
                item['type'],
                item['length'],
                item['performer'],
                item['country'],
                item['director'],
                item['show'],
                item['language'],
                item['score']
            )
            try:
                self.ora.cux_sql_base(self.ora.connect(), sql)
                # cursor.execute(sql, (name, low_price, high_price, ave_price, unit))
                # conn.commit()
            except Exception as e:
                print(str(e)+"  "+item['movie'])
