from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.history_gwas_result import HistoryGWAS


class TestGetErrorResultBB(unittest.TestCase):
    """历史记录-查询错误结果 BB端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestGetErrorResultBB START BB端')
        cls.node = 2
        cls.dh = DataHandle()
        # 布里端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.h_g = HistoryGWAS(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3501, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_get_Error_result_success(self):
        """BB 历史记录-查询错误结果 成功"""
        Log.debug('test_get_Error_result_success start')
        para_id = 35
        data_id = 35003
        res = self.h_g.base_get_error_result(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_Error_result_success end')
        pass

    def test_get_Error_result_no_session_fail(self):
        """BB 历史记录-查询错误结果 未登录，失败"""
        Log.debug('test_get_Error_result_no_session_fail start')
        para_id = 35
        data_id = 35004
        res = self.h_g.base_get_error_result(para_id=para_id, data_id=data_id, cookies=None,
                                             flag=False)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_Error_result_no_session_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestGetErrorResultBB END BB端')
