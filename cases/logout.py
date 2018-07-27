import json
import requests
from Base import Base
from log import Log
from dataHandle import DataHandle


class Logout(Base):

    def __init__(self, node=1, path_id=2):
        """ @:param node  1: hongkong other:bulisiban
            @:param p_id  path id
        """
        Base.__init__(self, node=node, path_id=path_id)

        pass

    def base_logout(self, para_id, data_id, cookies=None):
        """退出登录公共方法"""
        Log.info('logout url is %s' % self.url)
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        Log.info('request data is %s' % req_para)
        # 请求接口
        res = requests.post(url=self.url, headers=Base.headers, cookies=cookies,
                            data=json.dumps(req_para)).json()
        Log.info('logout response data is {}'.format(res))
        # 结果检查
        actual = self.check(res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    @staticmethod
    def check(res):
        """1 成功 0 失败"""
        return Base.check(res)


if __name__ == "__main__":
    h = Logout(1, 2)
    b = Logout(2, 2)
    print(Logout.check(b.logout(para_id=2, data_id=5).json()))
    print(Logout.check(Logout(2, 2).logout(para_id=2, data_id=5).json()))
    pass
