# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import datetime

from util.con_MySQL import Dba

logger = logging.getLogger(__name__)


class HomespiderPipeline(object):
    def __init__(self):
        # client = pymongo.MongoClient("192.168.20.216", 27017)
        # db = client["SinaWebchatWeather"]
        # self.sinaComment = db["SinaComment"]
        # self.sinaContent = db["SinaContent"]
        # self.sogou = db["SoGouContent"]
        # self.tweets = db["Tweets"]
        # self.Info = db["Information"]
        self.ora = Dba()
        self.CaiJia_Sql = """
            INSERT INTO HOME_CAIJIA(name, low_price, high_price, ave_price,unit,date) values('%s', '%s', '%s', '%s', '%s', now())
            """

    # pipeline默认调用
    def process_item(self, item, spider):
        # 创建数据库连接,格式为utf8
        # conn = pymysql.connect(
        #     host='localhost',
        #     user="root",
        #     passwd="root",
        #     db='test',
        #     charset="utf8",
        #     cursorclass=pymysql.cursors.DictCursor
        # )
        # with conn.cursor() as cursor:
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
        # finally:
        #     conn.close()

    # if __name__ == '__main__':
    #     item = HomespiderItem()
    #     item['name'] = '青菜'
    #     item['low_price'] = 2.12
    #     item['high_price'] = 4
    #     item['ave_price'] = 3.4
    #     item['unit'] = '元/公斤(kg)'
    #     # item['date'] = '2018-04-11'
    #     process_item("", item)
