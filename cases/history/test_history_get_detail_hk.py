from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.historytest import HistoryTest


class TestHistoryGetDetailHK(unittest.TestCase):
    """历史记录--查询详情 HK端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestHistoryGetDetailHK START HK端')
        cls.node = 1
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.h_t = HistoryTest(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_history_get_detail_success(self):
        """HK 历史记录-查询详情 成功"""
        Log.debug('test_history_get_detail_success start')
        para_id = 28
        data_id = 28001
        res = self.h_t.base_get_detail(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                       flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_history_get_detail_success end')
        pass

    def test_history_get_detail_no_session_fail(self):
        """HK 历史记录-查询详情 未登录，失败"""
        Log.debug('test_history_get_detail_no_session_fail start')
        para_id = 28
        data_id = 28002
        res = self.h_t.base_get_detail(para_id=para_id, data_id=data_id, cookies=None,
                                       flag=False)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_history_get_detail_no_session_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestHistoryGetDetailHK END HK端')
