from dataHandle import DataHandle
from loadConfig import LoadConfig
import time
# import requests
import hashlib
# from log import Log


class Base:
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}
    lc = LoadConfig()
    dh = DataHandle()

    def __init__(self, node=1, path_id=1):
        """ @:param node  1: hongkong other:bulisiban
            @:param p_id  path id
        """
        self.domain = self.lc.get_domain_h() if node == 1 else self.lc.get_domain_b()
        self.url = self.domain + self.dh.get_path(path_id)
        pass

    @staticmethod
    def res_check(res):
        """1 成功 0 失败"""
        if res["result"] == 0 and res["errCode"] is None:
            return 1
        else:
            return 0

    @classmethod
    def get_req_para(cls, para_id, data_id):
        para_source = cls.dh.get_para(para_id)
        cls.data_source = cls.dh.get_data(data_id)[0]
        req_para = DataHandle.combine_data(para_source, cls.data_source)
        return req_para

    @staticmethod
    def make_password(password):
        return hashlib.md5(password.encode('utf-8')).hexdigest()

    @staticmethod
    def gene_username():
        return 'test{}'.format(int(time.strftime("%Y%m%d%H%M%S")))


if __name__ == "__main__":
    print(Base.gene_username())
