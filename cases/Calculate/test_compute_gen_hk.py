from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.computegen import ComputeGen


class TestComputeGenHK(unittest.TestCase):
    """基因协同计算-HK端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestComputeGenHK START HK端')
        cls.node = 1
        # 计算类型  gen;2
        cls.calType = 2
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.comp_gen = ComputeGen(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_compute_gen_success(self):
        """HK 基因协同计算，成功"""
        Log.debug('test_compute_gen_success start')
        para_id = 23
        data_id = 23001
        res = self.comp_gen.base_compute_gen(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             calType=self.calType, max_server=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gen_success end')
        pass

    def test_compute_gen_no_session_fail(self):
        """HK 基因协同计算，未登录，失败"""
        Log.debug('test_compute_gen_no_session_fail start')
        para_id = 23
        data_id = 23002
        res = self.comp_gen.base_compute_gen(para_id=para_id, data_id=data_id, cookies=None,
                                             calType=self.calType, max_server=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gen_no_session_fail end')
        pass

    def test_compute_gen_taskId_not_exist_fail(self):
        """HK 基因协同计算，taskid不存在，失败"""
        Log.debug('test_compute_gen_taskId_not_exist_fail start')
        para_id = 23
        data_id = 23003
        res = self.comp_gen.base_compute_gen(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             calType=0, max_server=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gen_taskId_not_exist_fail end')
        pass

    def test_compute_gen_fileId_not_exist_fail(self):
        """HK 基因协同计算，serverId不存在，失败"""
        Log.debug('test_compute_gen_fileId_not_exist_fail start')
        para_id = 23
        data_id = 23004
        res = self.comp_gen.base_compute_gen(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             calType=self.calType, max_server=1)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gen_fileId_not_exist_fail end')
        pass

    def test_compute_gen_taskId_wrong_1_fail(self):
        """HK 基因协同计算，taskid为vcf的任务，失败"""
        Log.debug('test_compute_gen_taskId_wrong_2_fail start')
        para_id = 23
        data_id = 23005
        res = self.comp_gen.base_compute_gen(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             calType=1, max_server=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gen_taskId_wrong_2_fail end')
        pass

    def test_compute_gen_taskId_wrong_3_fail(self):
        """HK gen协同计算，taskid为GWAS的任务，失败"""
        Log.debug('test_compute_gen_taskId_wrong_3_fail start')
        para_id = 23
        data_id = 23006
        res = self.comp_gen.base_compute_gen(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                             calType=3, max_server=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_compute_gen_taskId_wrong_3_fail end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestComputeGenHK END HK端')
