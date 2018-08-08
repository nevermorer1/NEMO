from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.computevcf import ComputeVcf


class TestComputeVcfHK(unittest.TestCase):
    """vcf协同计算-HK端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestComputeVcfHK START HK端')
        cls.node = 1
        # 计算类型  vcf;1
        cls.calType = 1
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

    def test_compute_vcf_success(self):
        """HK vcf协同计算，成功"""
        Log.debug('test_compute_vcf_success start')
        para_id = 22
        data_id = 22001
        res = self.comp_vcf.base_compute_vcf(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             calType=self.calType, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_vcf_success end')
        pass

    def test_compute_vcf_no_session_fail(self):
        """HK vcf协同计算，未登录，失败"""
        Log.debug('test_compute_vcf_no_session_fail start')
        para_id = 22
        data_id = 22002
        res = self.comp_vcf.base_compute_vcf(para_id=para_id, data_id=data_id, cookies=None,
                                             calType=self.calType, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_vcf_no_session_fail end')
        pass

    def test_compute_vcf_taskId_not_exist_fail(self):
        """HK vcf协同计算，taskid不存在，失败"""
        Log.debug('test_compute_vcf_taskId_not_exist_fail start')
        para_id = 22
        data_id = 22003
        res = self.comp_vcf.base_compute_vcf(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             calType=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_vcf_taskId_not_exist_fail end')
        pass

    def test_compute_vcf_fileId_not_exist_fail(self):
        """HK vcf协同计算，fileid不存在，失败"""
        Log.debug('test_compute_vcf_fileId_not_exist_fail start')
        para_id = 22
        data_id = 22004
        res = self.comp_vcf.base_compute_vcf(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             calType=self.calType, maxFile=1)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_vcf_fileId_not_exist_fail end')
        pass

    def test_compute_vcf_taskId_wrong_2_fail(self):
        """HK vcf协同计算，taskid为基因协同计算的任务，失败"""
        Log.debug('test_compute_vcf_taskId_wrong_2_fail start')
        para_id = 22
        data_id = 22005
        res = self.comp_vcf.base_compute_vcf(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             calType=2, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_vcf_taskId_wrong_2_fail end')
        pass

    def test_compute_vcf_taskId_wrong_3_fail(self):
        """HK vcf协同计算，taskid为GWAS的任务，失败"""
        Log.debug('test_compute_vcf_taskId_wrong_3_fail start')
        para_id = 22
        data_id = 22006
        res = self.comp_vcf.base_compute_vcf(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             calType=3, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_vcf_taskId_wrong_3_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestComputeVcfHK END HK端')
