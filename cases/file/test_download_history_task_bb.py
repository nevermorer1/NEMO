from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.downloadfile import DownloadFile


class TestDownloadHistoryTaskBB(unittest.TestCase):
    """历史记录—下载文件"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestDownloadHistoryTaskBB START BB端')
        cls.node = 2
        cls.dh = DataHandle()
        # 布里端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.df = DownloadFile(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=4101, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_download_history_task_success(self):
        """BB 历史记录—下载文件 成功"""
        Log.debug('test_download_history_task_success start')
        para_id = 41
        data_id = 41003
        res = self.df.base_download_history_task(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                 flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_history_task_success end')
        pass

    def test_download_history_task_no_session_fail(self):
        """BB 历史记录—下载文件 未登录，失败"""
        Log.debug('test_download_history_task_no_session_fail start')
        para_id = 41
        data_id = 41004
        res = self.df.base_download_history_task(para_id=para_id, data_id=data_id, cookies=None,
                                                 flag=False)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_history_task_no_session_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestDownloadHistoryTaskBB END BB端')
