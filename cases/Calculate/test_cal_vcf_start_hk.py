from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.caculvcf import CalVcf


class TestVCFStartHK(unittest.TestCase):
    """vcf发起-HK端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestVCFStartHK START HK端')
        cls.node = 1
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.cal_vcf = CalVcf(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_vcf_start_1_file_success(self):
        """HK vcf数据集比较发起成功，单个文件"""
        Log.debug('test_vcf_start_1_file_success start')
        para_id = 11
        data_id = 11001
        res = self.cal_vcf.base_vcf_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_vcf_start_1_file_success end')
        pass

    def test_vcf_start_2_file_success(self):
        """HK vcf数据集比较发起成功,多个文件"""
        Log.debug('test_vcf_start_2_file_success start')
        para_id = 11
        data_id = 11002
        res = self.cal_vcf.base_vcf_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_vcf_start_2_file_success end')
        pass

    def test_vcf_start_no_session(self):
        """HK 未登录vcf数据集比较发起失败"""
        Log.debug('test_vcf_start_no_session start')
        para_id = 11
        data_id = 11003
        res = self.cal_vcf.base_vcf_start(para_id=para_id, data_id=data_id, cookies=None,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_vcf_start_no_session end')
        pass

    def test_vcf_start_empty_file(self):
        """HK vcf数据集比较,文件列表为空，发起失败"""
        Log.debug('test_vcf_start_empty_file start')
        para_id = 11
        data_id = 11004
        res = self.cal_vcf.base_vcf_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_vcf_start_empty_file end')
        pass

    def test_vcf_start_longer_remark(self):
        """HK vcf数据集比较发起,remark超长，发起失败"""
        Log.debug('test_vcf_start_longer_remark start')
        para_id = 11
        data_id = 11005
        res = self.cal_vcf.base_vcf_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=1, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_vcf_start_longer_remark end')
        pass

    def test_vcf_start_file_not_exist(self):
        """HK vcf数据集比较发起，文件id不存在，发起失败"""
        Log.debug('test_vcf_start_file_not_exist start')
        para_id = 11
        data_id = 11006
        res = self.cal_vcf.base_vcf_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=1)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_vcf_start_file_not_exist end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestVCFStartHK END HK端')
