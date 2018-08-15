from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.downloadfile import DownloadFile
from cases.userinfo import UserInfo


class TestDownloadLogFileHK(unittest.TestCase):
    """日志部分-下载log文件"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestDownloadLogFileHK START HK端')
        cls.node = 1
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.df = DownloadFile(node=cls.node)
        cls.ui = UserInfo(node=cls.node)
        # auto登录cookie
        cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_download_log_file_success(self):
        """HK 日志部分-下载log文件 成功"""
        Log.debug('test_download_log_file_success start')
        para_id = 43
        data_id = 43001
        res = self.df.base_download_log_file(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_log_file_success end')
        pass

    def test_download_log_file_no_session_fail(self):
        """HK 日志部分-下载log文件 未登录，失败"""
        Log.debug('test_download_log_file_no_session_fail start')
        para_id = 43
        data_id = 43002
        res = self.df.base_download_log_file(para_id=para_id, data_id=data_id, cookies=None,
                                             flag=False)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_log_file_no_session_fail end')
        pass

    def test_download_log_file_not_admin_fail(self):
        """HK 普通用户下载log失败"""
        Log.debug('test_download_log_file_not_admin_fail start')
        para_id = 43
        data_id = 43003
        res = self.df.base_download_log_file(para_id=para_id, data_id=data_id, cookies=self.AUTO_cookies,
                                             flag=False)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_log_file_not_admin_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestDownloadLogFileHK END HK端')
