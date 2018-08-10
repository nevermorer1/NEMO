from common.dataHandle import DataHandle
from common.loadConfig import LoadConfig
import time
import rsa
import hashlib
import base64
from common.log import Log
import collections
import json
import os


class Base:
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/66.0.3359.117 Safari/537.36'}
    lc = LoadConfig()
    dh = DataHandle()

    def __init__(self, node, path_id):
        """ @:param node  1: hongkong other:bulisiban
            @:param p_id  path id
        """

        self.domain = self.lc.get_domain_h() if node == 1 else self.lc.get_domain_b()
        self.url = self.domain + self.dh.get_path(path_id)
        pass

    @staticmethod
    def check(res):
        """1 成功 0 失败"""
        code = '00000'
        if res["code"] == code:
            Log.debug('actual res check is 1')
            return 1
        else:
            Log.debug('actual res check is 0')
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

    @staticmethod
    def order_dic_by_keys(data):
        """字典按key排序"""
        sorted_data = collections.OrderedDict()
        for key in sorted(data.keys()):
            sorted_data[key] = data[key]
        return sorted_data

    @staticmethod
    def sign(data):
        # 加签私钥
        keyfile = os.path.join(os.path.abspath('../config'), 'keyen.pem')
        pri_key = rsa.PrivateKey.load_pkcs1(keyfile=open(keyfile, 'r').read().encode())

        # 数据排序
        sorted_data = Base.order_dic_by_keys(data)
        # sorted_data = collections.OrderedDict()
        # for key in sorted(data.keys()):
        #     sorted_data[key] = data[key]

        str_data = json.dumps(sorted_data)
        # 去掉空格
        str_data = str_data.split()
        str_data = ''.join(str_data)
        # 签名
        signature = rsa.sign(str_data.encode(encoding='utf-8'), priv_key=pri_key, hash='SHA-1')
        sig = base64.b16encode(signature).lower().decode()
        res = {
            "msg": str_data,
            "signature": sig
        }
        Log.info('加签数据为：{}'.format(json.dumps(res)))
        return json.dumps(res)


if __name__ == "__main__":
    # print(Base.gene_username())
    data = {"target": "", "calType": "", "pageNo": 1, "pageSize": 20, "remark": ""}
    print(Base.sign(data))
