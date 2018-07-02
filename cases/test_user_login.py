from dataHandle import DataHandle
from loadConfig import LoadConfig
import unittest
import random
import hashlib
from log import Log


def make_password(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()


class TestUserLogin(unittest.TestCase):
    """8.2.3.用户登录"""

    @classmethod
    def setUpClass(cls):
        Log.debug('TestUserLogin START')
        cls.lc = LoadConfig()
        cls.domain = cls.lc.get_domain()
        cls.dh = DataHandle()
        cls.url = cls.lc.get_domain() + cls.dh.get_path(1)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_user_login(self):
        """test_user_login"""
        Log.info('request url is %s' % self.url)
        para_id = 1
        para_source = self.dh.get_para(para_id)
        data_source = self.dh.get_data(para_id)

        for i in range(len(data_source)):
            req_para = DataHandle.combine_data(para_source, data_source[i])
            req_para['password'] = make_password(req_para['password'])
            Log.info('request data is %s' % req_para)
            actual = random.randint(0, 1)
            actual = 0
            DataHandle.set_data(data_source[i], actual)
        self.dh.write_data(data_source)
        self.assertTrue(self.dh.check_result(data_source), msg="failed ,refer to result.csv")

    def test_001(self):
        Log.info('new test start')
        Log.info('new test end')

    def test_002(self):
        Log.info('new test start')
        Log.info('new test end')

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestUserLogin END')
