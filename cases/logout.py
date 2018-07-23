import json
import requests
from Base import Base
from log import Log


class Logout(Base):

    def __init__(self, node=1, path_id=2):
        """ @:param node  1: hongkong other:bulisiban
            @:param p_id  path id
        """
        Base.__init__(self, node=node, path_id=path_id)

        pass

    def logout(self, para_id, data_id, cookies=None):
        req_para = self.get_req_para(para_id, data_id)
        Log.info('logout url is %s' % self.url)
        Log.info('request data is %s' % req_para)
        res = requests.post(url=self.url, data=json.dumps(req_para), cookies=cookies,
                            headers=self.headers)
        return res

    @staticmethod
    def check(res):
        """1 成功 0 失败"""
        return Base.res_check(res)


if __name__ == "__main__":
    h = Logout(1, 2)
    b = Logout(2, 2)
    print(Logout.check(b.logout(para_id=2, data_id=5).json()))
    print(Logout.check(Logout(2, 2).logout(para_id=2, data_id=5).json()))
    pass
