# -*- coding:utf-8 -*-
import pymysql
from common.loadConfig import LoadConfig
from common.log import Log


class sql:
    def __init__(self, node=1):
        """node:1 hk, 2 bb"""
        self.lc = LoadConfig()
        self.section = 'sql_h' if node == 1 else 'sql_b'
        self.conf = self.lc.get_db_conf(section=self.section)
        pass

    def select_single(self, sql):
        return self.select(sql=sql)[0][0]

    def select(self, sql):
        conn = pymysql.connect(
            host=self.conf.get('host'),
            port=int(self.conf.get('port')),
            user=self.conf.get('user'),
            password=self.conf.get('password'),
            database=self.conf.get('database'),
        )
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def select_dic(self, sql):
        """返回字典"""
        conn = pymysql.connect(
            host=self.conf.get('host'),
            port=int(self.conf.get('port')),
            user=self.conf.get('user'),
            password=self.conf.get('password'),
            database=self.conf.get('database'),
            cursorclass=pymysql.cursors.DictCursor
        )
        cur = conn.cursor()
        try:
            cur.execute(sql)
            result = cur.fetchall()
            return result
        except:
            Log.error('select_dic error !')
        finally:
            cur.close()
            conn.close()

    def select_dic_single(self, sql):
        res = self.select_dic(sql=sql)[0]
        return res

    def updata(self, sql):
        conn = pymysql.connect(
            host=self.conf.get('host'),
            port=int(self.conf.get('port')),
            user=self.conf.get('user'),
            password=self.conf.get('password'),
            database=self.conf.get('database'),
        )
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
        except:
            # 发生错误回滚
            conn.rollback()
            Log.error("updata fail ! {}".format(sql))
        cur.close()
        conn.close()


if __name__ == '__main__':
    # s = sql()
    # ttt = 'SELECT * FROM t_user WHERE loginName = \'update\''
    # print(len(s.select(ttt)))
    pass
