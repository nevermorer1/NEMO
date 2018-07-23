from Base import Base
from login import Login
from log import Log
import requests
import json
from sql import sql


class UserInfo(Base):

    def __init__(self, node=1, path_id=1):
        """ @:param node  1: hongkong other:bulisiban
            @:param p_id  path id
        """
        self.cookies = Login(node=node, path_id=1).get_cookie()
        self.s = sql(node=node)
        Base.__init__(self, node=node, path_id=path_id)
        pass

    def insert_user(self, para_id, data_id, cookies):
        """新增用户"""
        # 获取请求url
        url_insert = self.domain + Base.dh.get_path(para_id)
        Log.info('insert user request url : {}'.format(url_insert))
        # 获取请求数据
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 随机生成用户名
        req_para['loginName'] = self.gene_username()
        req_para['name'] = self.gene_username()
        # 接口数据类型转换
        req_para['group'] = eval(req_para['group'])
        req_para['status'] = eval(req_para['status'])
        Log.info('insert user request data is {}'.format(json.dumps(req_para)))
        # 请求接口
        res = requests.post(url=url_insert, headers=Base.headers, cookies=cookies,
                            data=json.dumps(req_para))
        Log.info('insert user response data is {}'.format(res.json()))
        return res

    def login_modify(self,para_id, data_id,node=1,):
        auto_id = 3001
        L = Login(node=node)
        cookies_a = L.get_cookie(data_id=auto_id)
        # 获取请求url
        url_reset = self.domain + Base.dh.get_path(para_id)
        Log.info('modify_password url is {}'.format(url_reset))
        # 获取请求数据
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # md5
        req_para['password'] = Base.make_password(req_para['password'])
        req_para['newPassword'] = Base.make_password(req_para['newPassword'])
        Log.info('modify_password data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_reset, headers=Base.headers, cookies=cookies,
                            data=json.dumps(req_para))

        return res
        pass

    def modify_password(self,para_id, data_id,node=1):
        """修改用户密码"""
        sql_select = 'SELECT password FROM t_user WHERE loginName = \'Automation\''
        sql_update = 'UPDATE t_user SET `password`=bf WHERE loginName=\'Automation\''
        bf='1c18dc8afa0363def9fe4977dfff2f73'   #123456入库
        af='37b1a09078cf51963f48b478ab6efdf9'   #111111入库

        if bf == self.s.select(sql_select):
            self.login_modify(para_id, data_id,node)
        else:
            self.s.updata(sql)
            self.login_modify(para_id, data_id, node)
        pass

    def reset_password(self, para_id, data_id, cookies):
        """重置密码"""
        # 获取请求url
        url_reset = self.domain + Base.dh.get_path(para_id)
        Log.info('reset_password url is {}'.format(url_reset))
        # 获取请求数据
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        sql = 'SELECT id FROM t_user WHERE loginName = \'Automation\''
        # 设置 userid
        req_para['userId'] = self.s.select(sql)[0][0]
        Log.info('reset_password data is {}'.format(req_para))
        # 请求接口
        res = requests.post(url=url_reset, headers=Base.headers, cookies=cookies,
                            data=json.dumps(req_para))
        return res


if __name__ == '__main__':
    para1_id = 5
    data1_id = 5001
    UI = UserInfo(node=1, path_id=1)
    cookies = UI.cookies
    print(UI.reset_password(para_id=para1_id, data_id=data1_id,
                            cookies=cookies).json())
