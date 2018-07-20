from Base import Base
from login import Login
from log import Log
import requests
import json


class UserInfo(Base):

    def __init__(self, node=1, path_id=1):
        """ @:param node  1: hongkong other:bulisiban
            @:param p_id  path id
        """
        self.cookies = Login(node=node, path_id=1).get_cookie()
        Base.__init__(self, node=node, path_id=path_id)
        pass

    def insert_user(self, para_id, data_id, cookies):
        # 获取请求url
        url_insert = self.domain + Base.dh.get_path(para_id)
        Log.info('request url is {}'.format(url_insert))
        # 获取请求数据
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 随机生成用户名
        req_para['loginName'] = Base.gene_username()
        req_para['name'] = Base.gene_username()
        # 接口数据类型转换
        req_para['group'] = eval(req_para['group'])
        req_para['status'] = eval(req_para['status'])
        Log.info('insert user request data is {}'.format(req_para))
        # 请求接口
        res = requests.post(url=url_insert, headers=Base.headers, cookies=cookies,
                            data=json.dumps(req_para))
        Log.info('insert user response data is {}'.format(res.json()))
        return res


if __name__ == '__main__':
    para1_id = 9
    data1_id = 7
    UI = UserInfo(node=1, path_id=1)
    cookies = UI.cookies
    print(UI.insert_user(para_id=para1_id, data_id=data1_id,
                         cookies=cookies).json())
