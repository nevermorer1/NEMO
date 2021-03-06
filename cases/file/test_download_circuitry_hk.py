from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.downloadfile import DownloadFile


class TestDownloadCircuitryHK(unittest.TestCase):
    """逻辑管理-下载电路文件"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestDownloadCircuitryHK START HK端')
        cls.node = 1
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.df = DownloadFile(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=4201, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_download_circuitry_success(self):
        """HK 逻辑管理-下载电路文件 成功"""
        Log.debug('test_download_circuitry_success start')
        para_id = 42
        data_id = 42001
        res = self.df.base_download_circuitry(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                 flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_circuitry_success end')
        pass

    def test_download_circuitry_no_session_fail(self):
        """HK 逻辑管理-下载电路文件 未登录，失败"""
        Log.debug('test_download_circuitry_no_session_fail start')
        para_id = 42
        data_id = 42002
        res = self.df.base_download_circuitry(para_id=para_id, data_id=data_id, cookies=None,
                                                 flag=False)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_download_circuitry_no_session_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestDownloadCircuitryHK END HK端')
