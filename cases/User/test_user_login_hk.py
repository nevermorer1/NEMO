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
        self.login_base(data_id=data_id)
        Log.debug('test_login_success end')

    def test_login_wrong_pwd(self):
        """密码错误登录失败"""
        data_id = 2
        self.login_base(data_id=data_id)
        Log.debug('test_login_wrong_pwd end')

    def login_base(self, data_id):
        data_source = self.dh.get_data(data_id)
        res = self.L.login(data_id=data_id).json()
        Log.info('login response is {}'.format(res))
        # 登录检查
        actual = self.L.login_check(res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 断言结果检查
        self.assertTrue(self.dh.check_result(data_source), msg='result check fail')

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestUserLogin END HK 端')
