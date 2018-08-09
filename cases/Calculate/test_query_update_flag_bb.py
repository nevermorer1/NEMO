from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.canceltask import CancelTask


class TestQueryUpdateFlagBB(unittest.TestCase):
    """数据更新--BB端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestQueryUpdateFlagBB START BB端')
        cls.node = 2
        cls.dh = DataHandle()
        # 布里端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.cancel_task = CancelTask(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_query_success(self):
        """BB 数据更新成功"""
        Log.debug('test_query_success start')
        para_id = 25
        data_id = 25003
        res = self.cancel_task.base_query_update_flag(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                      flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_query_success end')
        pass

    def test_query_no_session_fail(self):
        """BB 未登录，数据更新失败"""
        Log.debug('test_query_no_session_fail start')
        para_id = 21
        data_id = 21004
        res = self.cancel_task.base_query_update_flag(para_id=para_id, data_id=data_id, cookies=None,
                                                      flag=False)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_query_no_session_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestQueryUpdateFlagBB END BB端')
