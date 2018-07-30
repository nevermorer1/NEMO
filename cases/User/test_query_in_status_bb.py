from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.userinfo import UserInfo


class TestQueryInStatusBB(unittest.TestCase):
    """本地查询在线状态-BB端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestQueryInStatusBB START BB端')
        cls.node = 2
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.ui = UserInfo(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_query_in_status(self):
        """BB 本地查询在线状态"""
        para_id = 4
        data_id = 4003
        res = self.ui.base_query_in_status(para_id=para_id, data_id=data_id,
                                           cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_query_in_status end')
        pass

    def test_query_in_status_no_session(self):
        """BB 未登录本地查询在线状态失败"""
        para_id = 4
        data_id = 4004
        res = self.ui.base_query_in_status(para_id=para_id, data_id=data_id,
                                           cookies=None)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_query_in_status_no_session end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestQueryInStatusBB END BB端')
