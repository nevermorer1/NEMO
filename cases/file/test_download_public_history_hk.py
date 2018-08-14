from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.downloadfile import DownloadFile


class TestDownloadPublicHistoryHK(unittest.TestCase):
    """历史记录—（批量）下载excel HK端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestDownloadPublicHistoryHK START HK端')
        cls.node = 1
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.df = DownloadFile(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=4001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_download_public_history_zh_CN_success(self):
        """HK 历史记录—（批量）下载excel 简体 成功"""
        Log.debug('test_download_public_history_zh_CN_success start')
        para_id = 40
        data_id = 40001
        res = self.df.base_download_public_history(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                   flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_public_history_zh_CN_success end')
        pass

    def test_download_public_history_zh_HK_success(self):
        """HK 历史记录—（批量）下载excel 繁体 成功"""
        Log.debug('test_download_public_history_zh_HK_success start')
        para_id = 40
        data_id = 40002
        res = self.df.base_download_public_history(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                   flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_public_history_zh_HK_success end')
        pass

    def test_download_public_history_en_US_success(self):
        """HK 历史记录—（批量）下载excel 英文 成功"""
        Log.debug('test_download_public_history_en_US_success start')
        para_id = 40
        data_id = 40003
        res = self.df.base_download_public_history(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                   flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_public_history_en_US_success end')
        pass

    def test_download_public_history_no_session_fail(self):
        """HK 历史记录—（批量）下载excel 未登录，失败"""
        Log.debug('test_download_public_history_no_session_fail start')
        para_id = 40
        data_id = 40004
        res = self.df.base_download_public_history(para_id=para_id, data_id=data_id, cookies=None,
                                                   flag=False)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_public_history_no_session_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestDownloadPublicHistoryHK END HK端')
