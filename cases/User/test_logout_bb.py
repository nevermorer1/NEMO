from common.dataHandle import DataHandle
from common.log import Log
from cases.logout import Logout
import unittest


class TestUserLogoutBB(unittest.TestCase):
    """用户登出 BB"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestUserLogoutBB START BB端')
        cls.node = 2
        cls.dh = DataHandle()
        # 布里端
        cls.LO = Logout(node=cls.node)
        # cls.admin_cookies = cls.L.get_cookie()

    def setUp(self):
        Log.debug('---------')
        pass

    def test_logout(self):
        """退出登录"""
        para_id = 2
        data_id = 2002
        res = self.LO.base_logout(para_id=para_id, data_id=data_id)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_logout end')

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestUserLogoutBB END BB端')
