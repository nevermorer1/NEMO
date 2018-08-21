from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.caculgen import CalGen


class TestGenStartBB(unittest.TestCase):
    """GEN发起-BB端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestGenStartBB START BB端')
        cls.node = 2
        cls.dh = DataHandle()
        # 布里端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.cal_gen = CalGen(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_gen_start_1_file_success(self):
        """BB 基因编辑距离对比发起成功，单个文件"""
        Log.debug('test_gen_start_1_file_success start')
        para_id = 13
        data_id = 13010
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_1_file_success end')
        pass

    def test_gen_start_2_file_success(self):
        """BB 基因编辑距离对比发起成功，多个文件"""
        Log.debug('test_gen_start_2_file_success start')
        para_id = 13
        data_id = 13011
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_2_file_success end')
        pass

    def test_gen_start_no_session(self):
        """BB 未登录，基因编辑距离对比发起失败"""
        Log.debug('test_gen_start_no_session start')
        para_id = 13
        data_id = 13012
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=None,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_no_session end')
        pass

    def test_gen_start_empty_file(self):
        """BB 文件列表为空，基因编辑距离对比发起失败"""
        Log.debug('test_gen_start_empty_file start')
        para_id = 13
        data_id = 13013
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_empty_file end')
        pass

    def test_gen_start_file_not_exist(self):
        """BB 文件id不存在，基因编辑距离对比发起失败"""
        Log.debug('test_gen_start_file_not_exist start')
        para_id = 13
        data_id = 13014
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=1)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_file_not_exist end')
        pass

    def test_gen_start_longer_remark(self):
        """BB remark超长，基因编辑距离对比发起失败"""
        Log.debug('test_gen_start_longer_remark start')
        para_id = 13
        data_id = 13015
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=1, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_longer_remark end')
        pass

    def test_gen_start_top_0(self):
        """BB top=0，基因编辑距离对比发起失败"""
        Log.debug('test_gen_start_top_0 start')
        para_id = 13
        data_id = 13016
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_top_0 end')
        pass

    def test_gen_start_top_3001(self):
        """BB top=3001，基因编辑距离对比发起失败"""
        Log.debug('test_gen_start_top_3001 start')
        para_id = 13
        data_id = 13017
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_top_3001 end')
        pass

    def test_gen_start_top_3000(self):
        """BB top=3000，基因编辑距离对比发起成功"""
        Log.debug('test_gen_start_top_3000 start')
        para_id = 13
        data_id = 13018
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_top_3000 end')
        pass

    def test_gen_status_1(self):
        """BB基因编辑距离对比发起状态测试，正确文件，发起后，双端状态为待接收"""
        Log.debug('test_gen_status_1 start')
        para_id = 13
        data_id = 13021
        res = self.cal_gen.base_gen_status(para_id=para_id, data_id=data_id,
                                           cookies=self.admin_cookies, )
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_status_1 end')
        pass

    def test_gen_status_6(self):
        """BB基因编辑距离对比发起状态测试，错误文件，发起后，双端状态为错误"""
        Log.debug('test_gen_status_6 start')
        para_id = 13
        data_id = 13022
        res = self.cal_gen.base_gen_status(para_id=para_id, data_id=data_id,
                                           cookies=self.admin_cookies, )
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_status_6 end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestGenStartBB END BB端')
