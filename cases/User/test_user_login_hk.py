from dataHandle import DataHandle
import unittest
from log import Log
from login import Login


class TestUserLoginHk(unittest.TestCase):
    """8.2.3.用户登录-香港端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestUserLogin START HK 端')
        # cls.lc = LoadConfig()
        # cls.domain = cls.lc.get_domain()
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=1)
        # cls.url = cls.lc.get_domain() + cls.dh.get_path(1)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_login_success(self):
        """用户登录成功"""
        data_id = 1
        para_id = 1
        data_source = self.dh.get_data(data_id)
        res = self.L.login(para_id=para_id, data_id=data_id).json()
        Log.info('login response is {}'.format(res))
        # 登录检查
        actual = self.L.login_check(res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 断言结果检查
        self.assertTrue(self.dh.check_result(data_source), msg='result check fail')
        Log.debug('test_login_success end')

    def test_login_wrong_pwd(self):
        """密码错误登录失败"""
        data_id = 2
        para_id = 1
        data_source = self.dh.get_data(data_id)
        res = self.L.login(para_id=para_id, data_id=data_id).json()
        Log.info('login response is {}'.format(res))
        # 登录检查
        actual = self.L.login_check(res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 断言结果检查
        self.assertTrue(self.dh.check_result(data_source), msg='result check fail')
        Log.debug('test_login_wrong_pwd end')

    def tearDown(self):
        Log.debug('---------')
        pass

    # demo
    # def test_user_login(self):
    #     """test_user_login"""
    #     Log.info('request url is %s' % self.url)
    #     para_id = 1
    #     para_source = self.dh.get_para(para_id)
    #     data_source = self.dh.get_data(para_id)
    #
    #     for i in range(len(data_source)):
    #         req_para = DataHandle.combine_data(para_source, data_source[i])
    #         Log.info('request data is %s' % req_para)
    #         actual = random.randint(0, 1)
    #
    #         DataHandle.set_data(data_source[i], actual)
    #     self.dh.write_data(data_source)
    #     self.assertTrue(self.dh.check_result(data_source), msg="failed ,refer to result.csv")

    @classmethod
    def tearDownClass(cls):
        Log.info('TestUserLogin END HK 端')