import json
import requests
from Base import Base
from log import Log


class Login(Base):

    def __init__(self, node=1, path_id=1):
        """ @:param node  1: hongkong other:bulisiban
            @:param p_id  path id
        """

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
        Log.info('request data is %s' % req_para)
        Log.info('login url is %s' % self.url)
        res = requests.post(url=self.url, data=json.dumps(req_para), headers=self.headers)
        return res

    @staticmethod
    def login_check(res):
        """1 成功 0 失败"""
        errcode = '00000'
        if res["result"] == 0 and res["errCode"] == errcode:
            return 1
        else:
            return 0

    def get_cookie(self, data_id=1):
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
