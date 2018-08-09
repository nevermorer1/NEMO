from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.computevcf import ComputeVcf


class TestComputeMulHK(unittest.TestCase):
    """vcf批量计算-HK端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestComputeMulHK START HK端')
        cls.node = 1
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.comp_vcf = ComputeVcf(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_compute_mul_success(self):
        """HK 批量计算成功，成功"""
        Log.debug('test_compute_mul_success start')
        para_id = 26
        data_id = 26001
        res = self.comp_vcf.base_compute_mul(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             flag=True,maxId=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_mul_success end')
        pass

    def test_compute_mul_no_session_fail(self):
        """HK 未登录，批量计算失败"""
        Log.debug('test_compute_mul_no_session_fail start')
        para_id = 26
        data_id = 26002
        res = self.comp_vcf.base_compute_mul(para_id=para_id, data_id=data_id, cookies=None,
                                             flag=False,maxId=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_mul_no_session_fail end')
        pass

    def test_compute_mul_taskId_not_exist_fail(self):
        """HK taskId不存在，批量计算失败"""
        Log.debug('test_compute_mul_taskId_not_exist_fail start')
        para_id = 26
        data_id = 26003
        res = self.comp_vcf.base_compute_mul(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             flag=False,maxId=1, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_mul_taskId_not_exist_fail end')
        pass

    def test_compute_mul_calType_2_fail(self):
        """HK calType=2，批量计算失败"""
        Log.debug('test_compute_mul_calType_2_fail start')
        para_id = 26
        data_id = 26004
        res = self.comp_vcf.base_compute_mul(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             flag=False,maxId=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_mul_calType_2_fail end')
        pass

    def test_compute_mul_file_not_exist_fail(self):
        """HK fileid不存在，批量计算失败"""
        Log.debug('test_compute_mul_file_not_exist_fail start')
        para_id = 26
        data_id = 26005
        res = self.comp_vcf.base_compute_mul(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             flag=False,maxId=0, maxFile=1)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_mul_file_not_exist_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestComputeMulHK END HK端')
