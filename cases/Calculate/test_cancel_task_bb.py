from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.canceltask import CancelTask


class TestCancelTaskBB(unittest.TestCase):
    """取消任务-BB端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestCancelTaskBB START BB端')
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

    def test_cancel_task_type_1_success(self):
        """BB 取消协同任务成功"""
        Log.debug('test_cancel_task_type_1_success start')
        para_id = 21
        data_id = 21008
        res = self.cancel_task.base_cancel_task(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                flag=True,task_modify=0, reason_modify=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_cancel_task_type_1_success end')
        pass

    def test_cancel_task_type_2_success(self):
        """BB 取消历史任务成功"""
        Log.debug('test_cancel_task_type_2_success start')
        para_id = 21
        data_id = 21009
        res = self.cancel_task.base_cancel_task(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                flag=True,task_modify=0, reason_modify=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_cancel_task_type_2_success end')
        pass

    def test_cancel_task_no_session_fail(self):
        """BB 未登录 取消任务失败"""
        Log.debug('test_cancel_task_no_session_fail start')
        para_id = 21
        data_id = 21010
        res = self.cancel_task.base_cancel_task(para_id=para_id, data_id=data_id, cookies=None,
                                                flag=False,task_modify=0, reason_modify=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_cancel_task_no_session_fail end')
        pass

    def test_cancel_task_task_id_not_exist_fail(self):
        """BB taskId不存在t_task，取消任务失败"""
        Log.debug('test_cancel_task_task_id_not_exist_fail start')
        para_id = 21
        data_id = 21011
        res = self.cancel_task.base_cancel_task(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                flag=False,task_modify=1, reason_modify=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_cancel_task_task_id_not_exist_fail end')
        pass

    def test_cancel_task_task_history_id_not_exist_fail(self):
        """BB taskId不存在t_task_history，取消任务失败"""
        Log.debug('test_cancel_task_task_history_id_not_exist_fail start')
        para_id = 21
        data_id = 21012
        res = self.cancel_task.base_cancel_task(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                flag=False,task_modify=1, reason_modify=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_cancel_task_task_history_id_not_exist_fail end')
        pass

    def test_cancel_task_reason_none_fail(self):
        """BB reason为空，取消任务失败"""
        Log.debug('test_cancel_task_reason_none_fail start')
        para_id = 21
        data_id = 21013
        res = self.cancel_task.base_cancel_task(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                flag=False,task_modify=0, reason_modify=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_cancel_task_reason_none_fail end')
        pass

    def test_cancel_task_reason_too_long_fail(self):
        """BB reason为超长，取消任务失败"""
        Log.debug('test_cancel_task_reason_too_long_fail start')
        para_id = 21
        data_id = 21014
        res = self.cancel_task.base_cancel_task(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                flag=False,task_modify=0, reason_modify=1)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_cancel_task_reason_too_long_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestCancelTaskBB END BB端')
