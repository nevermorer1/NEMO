from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.downloadfile import DownloadFile


class TestDownloadPublicTaskBB(unittest.TestCase):
    """协同计算详情下载excel BB端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestDownloadPublicTaskBB START BB端')
        cls.node = 2
        cls.dh = DataHandle()
        # 布里端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.df = DownloadFile(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3901, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_download_public_task_zh_CN_success(self):
        """BB 协同计算详情下载excel 简体 成功"""
        Log.debug('test_download_public_task_zh_CN_success start')
        para_id = 39
        data_id = 39005
        res = self.df.base_download_public_task(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_public_task_zh_CN_success end')
        pass

    def test_download_public_task_zh_BB_success(self):
        """BB 协同计算详情下载excel 繁体 成功"""
        Log.debug('test_download_public_task_zh_BB_success start')
        para_id = 39
        data_id = 39006
        res = self.df.base_download_public_task(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_public_task_zh_BB_success end')
        pass

    def test_download_public_task_en_US_success(self):
        """BB 协同计算详情下载excel 英文 成功"""
        Log.debug('test_download_public_task_en_US_success start')
        para_id = 39
        data_id = 39007
        res = self.df.base_download_public_task(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_public_task_en_US_success end')
        pass

    def test_download_public_task_no_session_fail(self):
        """BB 协同计算详情下载excel 未登录，失败"""
        Log.debug('test_download_public_task_no_session_fail start')
        para_id = 39
        data_id = 39008
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
        Log.info('TestDownloadPublicTaskBB END BB端')
