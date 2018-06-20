from dataHandle import DataHandle
from loadConfig import LoadConfig
import unittest
import random
import hashlib


def make_password(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()


class TestUserLogin(unittest.TestCase):
    """8.2.3.用户登录"""

    def setUp(self):
        self.lc = LoadConfig()
        self.domain = self.lc.get_domain()
        self.dh = DataHandle()
        self.url = self.lc.get_domain() + self.dh.get_path(1)
        pass

    def test_user_login(self):
        """test_user_login"""
        print('request url is %s' % self.url)
        para_id = 1
        para_source = self.dh.get_para(para_id)
        data_source = self.dh.get_data(para_id)

        for i in range(len(data_source)):
            req_para = DataHandle.combine_data(para_source, data_source[i])
            req_para['password'] = make_password(req_para['password'])
            print('request data is %s' % req_para)
            actual = random.randint(0, 1)
            DataHandle.set_data(data_source[i], actual)
        self.dh.write_data(data_source)
        self.assertTrue(self.dh.check_result(data_source), msg="failed ,refer to result.csv")
