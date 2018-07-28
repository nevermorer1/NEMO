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
    s = sql()
    sq = 'SELECT id FROM t_user WHERE loginName = \'Automation\''
    s.select(sq)
    pass
