from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.caculgen import CalGen


class TestGenStartHK(unittest.TestCase):
    """GEN发起-HK端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestGenStartHK START HK端')
        cls.node = 1
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.cal_gen = CalGen(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_gen_start_1_file_success(self):
        """HK 基因编辑距离对比发起成功，单个文件"""
        Log.debug('test_gen_start_1_file_success start')
        para_id = 13
        data_id = 13001
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_1_file_success end')
        pass

    def test_gen_start_2_file_success(self):
        """HK 基因编辑距离对比发起成功，多个文件"""
        Log.debug('test_gen_start_2_file_success start')
        para_id = 13
        data_id = 13002
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_2_file_success end')
        pass

    def test_gen_start_no_session(self):
        """HK 未登录，基因编辑距离对比发起失败"""
        Log.debug('test_gen_start_no_session start')
        para_id = 13
        data_id = 13003
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=None,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_no_session end')
        pass

    def test_gen_start_empty_file(self):
        """HK 文件列表为空，基因编辑距离对比发起失败"""
        Log.debug('test_gen_start_empty_file start')
        para_id = 13
        data_id = 13004
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_empty_file end')
        pass

    def test_gen_start_file_not_exist(self):
        """HK 文件id不存在，基因编辑距离对比发起失败"""
        Log.debug('test_gen_start_file_not_exist start')
        para_id = 13
        data_id = 13005
        res = res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                                isChange=0, maxFile=1)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_file_not_exist end')
        pass

    def test_gen_start_longer_remark(self):
        """HK remark超长，基因编辑距离对比发起失败"""
        Log.debug('test_gen_start_longer_remark start')
        para_id = 13
        data_id = 13006
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=1, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_longer_remark end')
        pass

    def test_gen_start_top_0(self):
        """HK top=0，基因编辑距离对比发起失败"""
        Log.debug('test_gen_start_top_0 start')
        para_id = 13
        data_id = 13007
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_top_0 end')
        pass

    def test_gen_start_top_3001(self):
        """HK top=3001，基因编辑距离对比发起失败"""
        Log.debug('test_gen_start_top_3001 start')
        para_id = 13
        data_id = 13008
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_top_3001 end')
        pass

    def test_gen_start_top_3000(self):
        """HK top=3000，基因编辑距离对比发起成功"""
        Log.debug('test_gen_start_top_3000 start')
        para_id = 13
        data_id = 13009
        res = self.cal_gen.base_gen_start(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                          isChange=0, maxFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_gen_start_top_3000 end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestGenStartHK END HK端')
