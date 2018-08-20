# -*- coding:utf-8 -*-
from common.sql import sql
from common.log import Log


class BeforeCheck:
    s_select_u = 'SELECT * FROM t_user WHERE loginName = \'update\''

    s_select_a = 'SELECT * FROM t_user WHERE loginName = \'Automation\''
    bf = '1c18dc8afa0363def9fe4977dfff2f73'  # Auto 123456入库
    s_update_a = "UPDATE t_user SET `password`= '%s' WHERE loginName=\'Automation\'" % bf

    def __init__(self, node=1):
        value_u = ('update', '9cea51579c586b57ab90a66ebc7f5c8a', node, 0)
        value_a = ('Automation', '1c18dc8afa0363def9fe4977dfff2f73', node, 0)
        self.s_insert_u = 'INSERT INTO t_user (`loginName`,`password`,`group`,`status`) VALUES {}'.format(value_u)
        self.s_insert_a = 'INSERT INTO t_user (`loginName`,`password`,`group`,`status`) VALUES {}'.format(value_a)
        self.s = sql(node=node)

    def check(self):
        # 检查update用户是否存在，不存在插入一条update用户数据
        if 0 == len(self.s.select(self.s_select_u)):
            Log.debug('update用户不存在，t_user表插入update:{}'.format(self.s_insert_u))
            self.s.updata(self.s_insert_u)
        # 检查Automation用户存在,不存在新增数据
        if 0 == len(self.s.select(self.s_select_a)):
            Log.debug('Automation用户不存在，t_user表插入update:{}'.format(self.s_insert_a))
            self.s.updata(self.s_insert_a)
        # 检查Automation用户初始密码是否为123456，不是则更改
        if self.bf != self.s.select_dic_single(self.s_select_a)['password']:
            Log.debug('Automation用户起始密码不为123456，更改为123456:{}'.format(self.s_update_a))
            self.s.updata(self.s_update_a)


if __name__ == '__main__':
    b = BeforeCheck()
    b.check()
