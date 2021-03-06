from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.caculget import CalGet


class TestGetDetailByAcceptBB(unittest.TestCase):
    """查询协同计算详情-BB端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestGetDetailByAcceptBB START BB端')
        cls.node = 2
        cls.dh = DataHandle()
        # 布里端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.cal_get = CalGet(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_get_detail_by_accept_success(self):
        """BB 查询详情，查询成功"""
        Log.debug('test_get_detail_by_accept_success start')
        para_id = 19
        data_id = 19003
        res = self.cal_get.base_get_detail_by_accept(para_id=para_id, data_id=data_id, cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_detail_by_accept_success end')
        pass

    def test_get_detail_by_accept_no_session_fail(self):
        """BB 查询详情，未登录，查询失败"""
        Log.debug('test_get_detail_by_accept_no_session_fail start')
        para_id = 19
        data_id = 19004
        res = self.cal_get.base_get_detail_by_accept(para_id=para_id, data_id=data_id, cookies=None)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_detail_by_accept_no_session_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestGetDetailByAcceptBB END BB端')
