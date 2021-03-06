import json
import requests
from common.Base import Base
from common.log import Log


class Login(Base):

    def __init__(self, node=1, path_id=1):
        """ @:param node  1: hongkong other:bulisiban
            @:param p_id  path id
        """
        # self.headers = {'Content-Type': 'application/json;charset=UTF-8'}
        self.path_id = path_id
        Base.__init__(self, node=node, path_id=path_id)
        # Log.info('login url is %s' % self.url)
        pass

    @classmethod
    def get_req_para(cls, para_id, data_id):
        req_para = Base.get_req_para(para_id, data_id)
        req_para['password'] = Base.make_password(req_para['password'])
        return req_para

    def login(self, data_id):
        req_para = self.get_req_para(para_id=self.path_id, data_id=data_id)
        Log.info('login data is %s' % json.dumps(req_para))
        Log.info('login url is %s' % self.url)
        res = requests.post(url=self.url, data=json.dumps(req_para), headers=self.headers)
        Log.info("login response is {}".format(res.json()))
        return res

    def login_sp(self, data):
        data['password'] = Base.make_password(data['password'])
        Log.info('login data is %s' % data)
        Log.info('login url is %s' % self.url)
        res = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        return res

    @staticmethod
    def login_check(res):
        """1 成功 0 失败"""
        code = '00000'
        if res["code"] == code:
            return 1
        else:
            return 0

    def get_cookie(self, data_id=1001):
        res = self.login(data_id=data_id)
        # return res.cookies
        # cookies = requests.utils.add_dict_to_cookiejar(cj=res.cookies,
        #                                                cookie_dict={"userInfo": res.json()['data']})
        cookies = res.cookies
        return cookies


if __name__ == "__main__":
    url = 'http://47.97.210.166/hkPro//history/queryUpdateFlag'
    data = {"pageNo": 1, "pageSize": 10, "taskId": 777}
    print(requests.post(url=url, headers=Base.headers, data=json.dumps(data),
                        cookies=Login.get_cookie()).json())
    pass
