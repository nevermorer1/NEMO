from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.caculget import CalGet


class TestGetServerHK(unittest.TestCase):
    """查询服务器-HK端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestGetServerHK START HK端')
        cls.node = 1
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.cal_get = CalGet(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_get_server_success(self):
        """HK 查询服务器，查询成功"""
        Log.debug('test_get_server_success start')
        para_id = 20
        data_id = 20001
        res = self.cal_get.base_get_server(para_id=para_id, data_id=data_id, cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_server_success end')
        pass

    def test_get_server_no_session_fail(self):
        """HK 查询服务器，未登录，查询失败"""
        Log.debug('test_get_server_no_session_fail start')
        para_id = 20
        data_id = 20002
        res = self.cal_get.base_get_server(para_id=para_id, data_id=data_id, cookies=None)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_server_no_session_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestGetServerHK END HK端')
