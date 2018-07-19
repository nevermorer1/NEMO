from Base import Base
from login import Login
from log import Log
import requests
import json


class UserInfo(Base):
    cookie = Login.get_cookie()

    def __init__(self, node=1, path_id=1):
        """ @:param node  1: hongkong other:bulisiban
            @:param p_id  path id
        """
        Base.__init__(self, node=node, path_id=path_id)
        pass

    def insert_user(self, para_id, data_id, cookies):
        # 获取请求url
        url_insert = self.domain + Base.dh.get_path(para_id)
        # 获取请求数据
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 随机生成用户名
        req_para['loginName'] = Base.gene_username()
        req_para['name'] = Base.gene_username()
        Log.info('insert user request data is {}'.format(req_para))
        # 请求接口
        res = requests.post(url=url_insert, headers=Base.headers, cookies=cookies,
                            data=json.dumps(req_para))
        return res


if __name__ == '__main__':
    para1_id = 9
    data1_id = 7
    cookie = UserInfo.cookie
    print(UserInfo().insert_user(para_id=para1_id, data_id=data1_id,
                                 cookies=cookie).json())
