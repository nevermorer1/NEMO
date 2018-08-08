from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.computegwas import ComputeGwas


class TestComputeGwasBB(unittest.TestCase):
    """GWAS协同计算-BB端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestComputeGwasBB START BB端')
        cls.node = 2
        # 计算类型  gwas;3
        cls.calType = 3
        cls.dh = DataHandle()
        # 布里端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.comp_gwas = ComputeGwas(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_compute_gwas_success(self):
        """BB GWAS协同计算，成功"""
        Log.debug('test_compute_gwas_success start')
        para_id = 24
        data_id = 24010
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               calType=self.calType, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_success end')
        pass

    def test_compute_gwas_no_session_fail(self):
        """BB GWAS协同计算，未登录，失败"""
        Log.debug('test_compute_gwas_no_session_fail start')
        para_id = 24
        data_id = 24011
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=None,
                                               calType=self.calType, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_no_session_fail end')
        pass

    def test_compute_gwas_taskId_not_exist_fail(self):
        """BB GWAS协同计算，taskid不存在，失败"""
        Log.debug('test_compute_gwas_taskId_not_exist_fail start')
        para_id = 24
        data_id = 24012
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               calType=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_taskId_not_exist_fail end')
        pass

    def test_compute_gwas_fileId_not_exist_fail(self):
        """BB GWAS协同计算，fileid不存在，失败"""
        Log.debug('test_compute_gwas_fileId_not_exist_fail start')
        para_id = 24
        data_id = 24013
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               calType=self.calType, maxFile=1)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_fileId_not_exist_fail end')
        pass

    def test_compute_gwas_file_lenth_is_0_fail(self):
        """BB GWAS协同计算，fileIdList长度为0，失败"""
        Log.debug('test_compute_gwas_file_lenth_is_0_fail start')
        para_id = 24
        data_id = 24014
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               calType=self.calType, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_file_lenth_is_0_fail end')
        pass

    def test_compute_gwas_file_lenth_is_1_fail(self):
        """BB GWAS协同计算，fileIdList长度为1，失败"""
        Log.debug('test_compute_gwas_file_lenth_is_1_fail start')
        para_id = 24
        data_id = 24015
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               calType=self.calType, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_file_lenth_is_1_fail end')
        pass

    def test_compute_gwas_file_lenth_is_3_fail(self):
        """BB GWAS协同计算，fileIdList长度为3，失败"""
        Log.debug('test_compute_gwas_file_lenth_is_3_fail start')
        para_id = 24
        data_id = 24016
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               calType=self.calType, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_file_lenth_is_3_fail end')
        pass

    def test_compute_gwas_taskId_wrong_1_fail(self):
        """BB GWAS协同计算，taskid为vcf的任务，失败"""
        Log.debug('test_compute_gwas_taskId_wrong_1_fail start')
        para_id = 24
        data_id = 24017
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               calType=1, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_taskId_wrong_1_fail end')
        pass

    def test_compute_gwas_taskId_wrong_2_fail(self):
        """BB GWAS协同计算，taskid为基因编辑距离的任务，失败"""
        Log.debug('test_compute_gwas_taskId_wrong_2_fail start')
        para_id = 24
        data_id = 24018
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               calType=2, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_taskId_wrong_2_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestComputeGwasBB END BB端')
