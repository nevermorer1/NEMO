from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.caculvcf import CalVcf


class TestVCFStartBB(unittest.TestCase):
    """vcf发起-BB端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestVCFStartBB START BB端')
        cls.node = 2
        cls.dh = DataHandle()
        # 布里端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.cal_vcf = CalVcf(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_vcf_start_1_file_success(self):
        """BB vcf数据集比较发起成功，单个文件"""
        Log.debug('test_vcf_start_1_file_success start')
        para_id = 11
        data_id = 11007
        res = self.cal_vcf.base_vcf_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_vcf_start_1_file_success end')
        pass

    def test_vcf_start_2_file_success(self):
        """BB vcf数据集比较发起成功,多个文件"""
        Log.debug('test_vcf_start_2_file_success start')
        para_id = 11
        data_id = 11008
        res = self.cal_vcf.base_vcf_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_vcf_start_2_file_success end')
        pass

    def test_vcf_start_no_session(self):
        """BB 未登录vcf数据集比较发起失败"""
        Log.debug('test_vcf_start_no_session start')
        para_id = 11
        data_id = 11009
        res = self.cal_vcf.base_vcf_start(para_id=para_id, data_id=data_id, cookies=None,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_vcf_start_no_session end')
        pass

    def test_vcf_start_empty_file(self):
        """BB vcf数据集比较,文件列表为空，发起失败"""
        Log.debug('test_vcf_start_empty_file start')
        para_id = 11
        data_id = 11010
        res = self.cal_vcf.base_vcf_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_vcf_start_empty_file end')
        pass

    def test_vcf_start_longer_remark(self):
        """BB vcf数据集比较发起,remark超长，发起失败"""
        Log.debug('test_vcf_start_longer_remark start')
        para_id = 11
        data_id = 11011
        res = self.cal_vcf.base_vcf_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=1, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_vcf_start_longer_remark end')
        pass

    def test_vcf_start_file_not_exist(self):
        """BB vcf数据集比较发起，文件id不存在，发起失败"""
        Log.debug('test_vcf_start_file_not_exist start')
        para_id = 11
        data_id = 11012
        res = self.cal_vcf.base_vcf_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=1)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_vcf_start_file_not_exist end')
        pass

    def test_vcf_status_1(self):
        """BB vcf状态测试，正确文件，发起后，双端状态为待接收"""
        Log.debug('test_vcf_status_1 start')
        para_id = 11
        data_id = 11015
        res = self.cal_vcf.base_vcf_status(para_id=para_id, data_id=data_id,
                                           cookies=self.admin_cookies,)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_vcf_status_1 end')
        pass

    def test_vcf_status_6(self):
        """BBvcf状态测试，错误文件，发起后，双端状态为错误"""
        Log.debug('test_vcf_status_6 start')
        para_id = 11
        data_id = 11016
        res = self.cal_vcf.base_vcf_status(para_id=para_id, data_id=data_id,
                                           cookies=self.admin_cookies,)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_vcf_status_6 end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestVCFStartBB END BB端')
