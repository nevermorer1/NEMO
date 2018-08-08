from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.computegwas import ComputeGwas


class TestComputeGwasHK(unittest.TestCase):
    """GWAS协同计算-HK端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestComputeGwasHK START HK端')
        cls.node = 1
        # 计算类型  gwas;3
        cls.calType = 3
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.comp_gwas = ComputeGwas(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_compute_gwas_success(self):
        """HK GWAS协同计算，成功"""
        Log.debug('test_compute_gwas_success start')
        para_id = 24
        data_id = 24001
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               calType=self.calType, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_success end')
        pass

    def test_compute_gwas_no_session_fail(self):
        """HK GWAS协同计算，未登录，失败"""
        Log.debug('test_compute_gwas_no_session_fail start')
        para_id = 24
        data_id = 24002
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=None,
                                               calType=self.calType, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_no_session_fail end')
        pass

    def test_compute_gwas_taskId_not_exist_fail(self):
        """HK GWAS协同计算，taskid不存在，失败"""
        Log.debug('test_compute_gwas_taskId_not_exist_fail start')
        para_id = 24
        data_id = 24003
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               calType=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_taskId_not_exist_fail end')
        pass

    def test_compute_gwas_fileId_not_exist_fail(self):
        """HK GWAS协同计算，fileid不存在，失败"""
        Log.debug('test_compute_gwas_fileId_not_exist_fail start')
        para_id = 24
        data_id = 24004
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               calType=self.calType, maxFile=1)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_fileId_not_exist_fail end')
        pass

    def test_compute_gwas_file_lenth_is_0_fail(self):
        """HK GWAS协同计算，fileIdList长度为0，失败"""
        Log.debug('test_compute_gwas_file_lenth_is_0_fail start')
        para_id = 24
        data_id = 24005
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               calType=self.calType, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_file_lenth_is_0_fail end')
        pass

    def test_compute_gwas_file_lenth_is_1_fail(self):
        """HK GWAS协同计算，fileIdList长度为1，失败"""
        Log.debug('test_compute_gwas_file_lenth_is_1_fail start')
        para_id = 24
        data_id = 24006
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               calType=self.calType, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_file_lenth_is_1_fail end')
        pass

    def test_compute_gwas_file_lenth_is_3_fail(self):
        """HK GWAS协同计算，fileIdList长度为3，失败"""
        Log.debug('test_compute_gwas_file_lenth_is_3_fail start')
        para_id = 24
        data_id = 24007
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               calType=self.calType, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_file_lenth_is_3_fail end')
        pass

    def test_compute_gwas_taskId_wrong_1_fail(self):
        """HK GWAS协同计算，taskid为vcf的任务，失败"""
        Log.debug('test_compute_gwas_taskId_wrong_1_fail start')
        para_id = 24
        data_id = 24008
        res = self.comp_gwas.base_compute_gwas(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                               calType=1, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gwas_taskId_wrong_1_fail end')
        pass

    def test_compute_gwas_taskId_wrong_2_fail(self):
        """HK GWAS协同计算，taskid为基因编辑距离的任务，失败"""
        Log.debug('test_compute_gwas_taskId_wrong_2_fail start')
        para_id = 24
        data_id = 24009
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
        Log.info('TestComputeGwasHK END HK端')
