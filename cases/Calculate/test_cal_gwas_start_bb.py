from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.caculgwas import CalGwas


class TestGwasStartBB(unittest.TestCase):
    """Gwas发起-BB端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestGwasStartBB START BB端')
        cls.node = 2
        cls.dh = DataHandle()
        # 布里端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.cal_gwas = CalGwas(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_gwas_start_2_file_success(self):
        """BB gwas发起成功，2个文件"""
        Log.debug('test_gwas_start_1_file_success start')
        para_id = 15
        data_id = 15012
        res = self.cal_gwas.base_gwas_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                            isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gwas_start_1_file_success end')
        pass

    def test_gwas_start_1_file_fail(self):
        """BB gwas发起失败，1个文件"""
        Log.debug('test_gwas_start_1_file_fail start')
        para_id = 15
        data_id = 15013
        res = self.cal_gwas.base_gwas_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                            isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gwas_start_1_file_fail end')
        pass

    def test_gwas_start_3_file_fail(self):
        """BB gwas发起失败，3个文件"""
        Log.debug('test_gwas_start_3_file_fail start')
        para_id = 15
        data_id = 15014
        res = self.cal_gwas.base_gwas_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                            isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gwas_start_3_file_fail end')
        pass

    def test_gwas_start_0_file_fail(self):
        """BB gwas发起失败，0个文件"""
        Log.debug('test_gwas_start_0_file_fail start')
        para_id = 15
        data_id = 15015
        res = self.cal_gwas.base_gwas_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                            isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gwas_start_0_file_fail end')
        pass

    def test_gwas_start_empty_file_fail(self):
        """BB gwas发起失败，文件不存在"""
        Log.debug('test_gwas_start_empty_file_fail start')
        para_id = 15
        data_id = 15016
        res = self.cal_gwas.base_gwas_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                            isChange=0, maxFile=1)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gwas_start_empty_file_fail end')
        pass

    def test_gwas_start_no_session(self):
        """BB gwas发起失败,未登录"""
        Log.debug('test_gwas_start_no_session start')
        para_id = 15
        data_id = 15017
        res = self.cal_gwas.base_gwas_start(para_id=para_id, data_id=data_id, cookies=None,
                                            isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gwas_start_no_session end')
        pass

    def test_gwas_start_longer_remark(self):
        """BB remark超长，gwas发起失败"""
        Log.debug('test_gwas_start_longer_remark start')
        para_id = 15
        data_id = 15018
        res = self.cal_gwas.base_gwas_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                            isChange=1, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gwas_start_longer_remark end')
        pass

    def test_gwas_start_none_logicType(self):
        """BB gwas发起失败，logicType为空"""
        Log.debug('test_gwas_start_none_logicType start')
        para_id = 15
        data_id = 15019
        res = self.cal_gwas.base_gwas_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                            isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gwas_start_none_logicType end')
        pass

    def test_gwas_start_ill_logicType(self):
        """BB gwas发起失败，logicType非法"""
        Log.debug('test_gwas_start_ill_logicType start')
        para_id = 15
        data_id = 15020
        res = self.cal_gwas.base_gwas_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                            isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gwas_start_ill_logicType end')
        pass

    def test_gwas_start_4_logicType_success(self):
        """BB gwas发起成功，logicType多个"""
        Log.debug('test_gwas_start_4_logicType_success start')
        para_id = 15
        data_id = 15021
        res = self.cal_gwas.base_gwas_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                            isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gwas_start_4_logicType_success end')
        pass

    def test_gwas_start_5_logicType_fail(self):
        """BB gwas发起成功，logicType超过4个"""
        Log.debug('test_gwas_start_5_logicType_fail start')
        para_id = 15
        data_id = 15022
        res = self.cal_gwas.base_gwas_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                            isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gwas_start_5_logicType_fail end')
        pass

    def test_gwas_status_1(self):
        """BB基因编辑距离对比发起状态测试，正确文件，发起后，双端状态为待接收"""
        Log.debug('test_gwas_status_1 start')
        para_id = 15
        data_id = 15025
        res = self.cal_gwas.base_gwas_status(para_id=para_id, data_id=data_id,
                                             cookies=self.admin_cookies)

        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gwas_status_1 end')
        pass

    # @unittest.skip('未检测，跳过执行')
    def test_gwas_status_6(self):
        """BB基因编辑距离对比发起状态测试，错误文件，发起后，双端状态为错误"""
        Log.debug('test_gwas_status_6 start')
        para_id = 15
        data_id = 15026
        res = self.cal_gwas.base_gwas_status(para_id=para_id, data_id=data_id,
                                             cookies=self.admin_cookies)

        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gwas_status_6 end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestGwasStartBB END BB端')
