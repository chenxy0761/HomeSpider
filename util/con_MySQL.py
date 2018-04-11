# -*- coding:utf-8 -*-

import os

import pymysql

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class Dba(object):

    def __init__(self):
        pass

    def connect(self):
        # 创建数据库连接,格式为utf8
        db = pymysql.connect(
            host='localhost',
            user="root",
            passwd="root",
            db='test',
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        return db

    def cursor(self):
        consor = self.connect().cursor()
        return consor

    def query(self, date):
        sql = """select DISTINCT type01,type03,dta_date from 
              qxj.qxj_info_news_list where flag=0 and dta_date > date'%s'""" % date
        cursor = self.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        self.close()
        return data

    def query_data(self, sql):
        cursor = self.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        self.close()
        return data

    def cux_sql(self, db, sql, name, date):
        cursor = db.cursor()
        Sql = """select * from HOME_CAIJIA where name = '%s' and date = '%s'""" % (
            name, date)
        cursor.execute(Sql)
        repetition = cursor.fetchone()
        if repetition:
            pass
        else:
            cursor.execute(sql)
            cursor.close()
            db.commit()

    def cux_sql_wechat(self, db, sql, id, date):
        cursor = db.cursor()
        Sql = """select * from QXJ.QXJ_YQ_READNUM_DAY where id = '%s' and dta_date = to_date('%s','yyyy-mm-dd')""" % (
            id, date)
        cursor.execute(Sql)
        repetition = cursor.fetchone()
        if repetition:
            pass
        else:
            cursor.execute(sql)
            cursor.close()
            db.commit()
            pass

    def close(self):
        self.cursor().connection.commit()
        self.cursor().close()
        self.connect().close()

# if __name__ == "__main__":
# print len(Dba().query("2017-10-01"))
# for i in Dba().query("2017-10-01"):
#     print i[0], i[1]
# db = Dba()
# print len(db.query())
# sql = "select dta_date,COUNT (type03) from qxj.qxj_info_news_list where flag = 1 AND dta_date >= date'2017-12-01' GROUP BY dta_date"
# sql = "select dta_date,COUNT (contentid) from QXJ.QXJ_YQ_WEIBO_DAY where flag = 1 AND dta_date >= date'2017-12-01' GROUP BY dta_date"
# sql = "select *  from system.help"
# cursor = db.cursor()
# cursor.execute(sql)
# for i in cursor.fetchall():
#     print(i[0], i[1], i[2])

# sql = "select * from  qxj.qxj_keyword_all_day"
# cursor = db.cursor()
# cursor.execute(sql)
# for i in cursor.fetchall():
#     print i
