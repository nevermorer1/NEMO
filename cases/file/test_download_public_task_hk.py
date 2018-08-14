from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.downloadfile import DownloadFile


class TestDownloadPublicTaskHK(unittest.TestCase):
    """协同计算详情下载excel HK端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestDownloadPublicTaskHK START HK端')
        cls.node = 1
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.df = DownloadFile(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3901, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_download_public_task_zh_CN_success(self):
        """HK 协同计算详情下载excel 简体 成功"""
        Log.debug('test_download_public_task_zh_CN_success start')
        para_id = 39
        data_id = 39001
        res = self.df.base_download_public_task(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_public_task_zh_CN_success end')
        pass

    def test_download_public_task_zh_HK_success(self):
        """HK 协同计算详情下载excel 繁体 成功"""
        Log.debug('test_download_public_task_zh_HK_success start')
        para_id = 39
        data_id = 39002
        res = self.df.base_download_public_task(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_public_task_zh_HK_success end')
        pass

    def test_download_public_task_en_US_success(self):
        """HK 协同计算详情下载excel 英文 成功"""
        Log.debug('test_download_public_task_en_US_success start')
        para_id = 39
        data_id = 39003
        res = self.df.base_download_public_task(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_public_task_en_US_success end')
        pass

    def test_download_public_task_no_session_fail(self):
        """HK 协同计算详情下载excel 未登录，失败"""
        Log.debug('test_download_public_task_no_session_fail start')
        para_id = 39
        data_id = 39004
        res = self.df.base_download_public_task(para_id=para_id, data_id=data_id, cookies=None,
                                                flag=False)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_public_task_no_session_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestDownloadPublicTaskHK END HK端')
