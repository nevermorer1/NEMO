from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.history_gwas_result import HistoryGWAS


class TestGetGwasResultHK(unittest.TestCase):
    """历史记录-查询基因编辑距离对比计算结果 HK端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestGetGwasResultHK START HK端')
        cls.node = 1
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.h_g = HistoryGWAS(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3101, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_get_maf_result_success(self):
        """HK 历史记录-查询maf计算结果 成功"""
        Log.debug('test_get_maf_result_success start')
        para_id = 31
        data_id = 31001
        res = self.h_g.base_get_maf_cal_result(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_maf_result_success end')
        pass

    def test_get_maf_result_no_session_fail(self):
        """HK 历史记录-查询maf计算结果 未登录，失败"""
        Log.debug('test_get_maf_result_no_session_fail start')
        para_id = 31
        data_id = 31002
        res = self.h_g.base_get_maf_cal_result(para_id=para_id, data_id=data_id, cookies=None,
                                               flag=False)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_maf_result_no_session_fail end')
        pass

    def test_get_gwasgen_result_success(self):
        """HK 历史记录-查询gwasgen计算结果 成功"""
        Log.debug('test_get_gwasgen_result_success start')
        para_id = 32
        data_id = 32001
        res = self.h_g.base_get_gwasgen_cal_result(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                   flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_gwasgen_result_success end')
        pass

    def test_get_gwasgen_result_no_session_fail(self):
        """HK 历史记录-查询gwasgen计算结果 未登录，失败"""
        Log.debug('test_get_gwasgen_result_no_session_fail start')
        para_id = 32
        data_id = 32002
        res = self.h_g.base_get_gwasgen_cal_result(para_id=para_id, data_id=data_id, cookies=None,
                                                   flag=False)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_gwasgen_result_no_session_fail end')
        pass

    def test_get_Dominant_result_success(self):
        """HK 历史记录-查询Dominant显性计算结果 成功"""
        Log.debug('test_get_Dominant_result_success start')
        para_id = 33
        data_id = 33001
        res = self.h_g.base_get_Dominant_cal_result(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                    flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_Dominant_result_success end')
        pass

    def test_get_Dominant_result_no_session_fail(self):
        """HK 历史记录-查询Dominant显性计算结果 未登录，失败"""
        Log.debug('test_get_Dominant_result_no_session_fail start')
        para_id = 33
        data_id = 33002
        res = self.h_g.base_get_Dominant_cal_result(para_id=para_id, data_id=data_id, cookies=None,
                                                    flag=False)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_Dominant_result_no_session_fail end')
        pass

    def test_get_Recessive_result_success(self):
        """HK 历史记录-查询Recessive隐性计算结果 成功"""
        Log.debug('test_get_Recessive_result_success start')
        para_id = 34
        data_id = 34001
        res = self.h_g.base_get_Recessive_cal_result(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                    flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_Recessive_result_success end')
        pass

    def test_get_Recessive_result_no_session_fail(self):
        """HK 历史记录-查询Recessive隐性计算结果 未登录，失败"""
        Log.debug('test_get_Recessive_result_no_session_fail start')
        para_id = 34
        data_id = 34002
        res = self.h_g.base_get_Recessive_cal_result(para_id=para_id, data_id=data_id, cookies=None,
                                                    flag=False)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_Recessive_result_no_session_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestGetGwasResultHK END HK端')
