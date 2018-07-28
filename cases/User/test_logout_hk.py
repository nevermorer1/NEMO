from common.dataHandle import DataHandle
from common.log import Log
from cases.logout import Logout
import unittest


class TestUserLogoutHK(unittest.TestCase):
    """用户登出 HK"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestUserLogoutHK START HK端')
        cls.node = 1
        cls.dh = DataHandle()
        # 香港端
        cls.LO = Logout(node=cls.node)
        # cls.admin_cookies = cls.L.get_cookie()

    def tearDown(self):
        Log.debug('---------')
        pass

    def setUp(self):
        Log.debug('---------')
        pass

    def test_logout(self):
        """退出登录"""
        para_id = 2
        data_id = 2001
        res = self.LO.base_logout(para_id=para_id, data_id=data_id)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_logout end')

    @classmethod
    def tearDownClass(cls):
        Log.info('TestUserLogoutHK END HK端')
