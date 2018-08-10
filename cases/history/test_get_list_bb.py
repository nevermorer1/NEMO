from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.historytest import HistoryTest


class TestGetListBB(unittest.TestCase):
    """历史记录--查询协同任务列表-BB端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestGetListBB START BB端')
        cls.node = 2
        cls.dh = DataHandle()
        # 布里端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.h_t = HistoryTest(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_get_list_all_success(self):
        """BB 查询协同任务列表，全部数据，成功"""
        Log.debug('test_get_list_all_success start')
        para_id = 27
        data_id = 27018
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_all_success end')
        pass

    def test_get_list_no_session_fail(self):
        """BB 查询协同任务列表 全部 未登录，查询失败"""
        Log.debug('test_get_list_no_session_fail start')
        para_id = 27
        data_id = 27019
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=None,
                                     flag=False)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_no_session_fail end')
        pass

    def test_get_list_vcf_success(self):
        """BB 查询协同任务列表，vcf，成功"""
        Log.debug('test_get_list_vcf_success start')
        para_id = 27
        data_id = 27020
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_vcf_success end')
        pass

    def test_get_list_gen_success(self):
        """BB 查询协同任务列表，基因，成功"""
        Log.debug('test_get_list_gen_success start')
        para_id = 27
        data_id = 27021
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_gen_success end')
        pass

    def test_get_list_gwas_success(self):
        """BB 查询协同任务列表 GWAS计算 查询成功"""
        Log.debug('test_get_list_gwas_success start')
        para_id = 27
        data_id = 27022
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_gwas_success end')
        pass

    def test_get_list_init_BB_success(self):
        """BB 查询协同任务列表，香港发起，成功"""
        Log.debug('test_get_list_init_BB_success start')
        para_id = 27
        data_id = 27023
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_init_BB_success end')
        pass

    def test_get_list_init_bb_success(self):
        """BB 查询协同任务列表，布里发起，成功"""
        Log.debug('test_get_list_init_bb_success start')
        para_id = 27
        data_id = 27024
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_init_bb_success end')
        pass

    def test_get_list_status_1_success(self):
        """BB 查询协同任务列表，待接收，成功"""
        Log.debug('test_get_list_status_1_success start')
        para_id = 27
        data_id = 27025
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_status_1_success end')
        pass

    def test_get_list_status_2_success(self):
        """BB 查询协同任务列表，计算中，成功"""
        Log.debug('test_get_list_status_2_success start')
        para_id = 27
        data_id = 27026
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_status_2_success end')
        pass

    def test_get_list_status_3_success(self):
        """BB 查询协同任务列表，已完成，成功"""
        Log.debug('test_get_list_status_3_success start')
        para_id = 27
        data_id = 27027
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_status_3_success end')
        pass

    def test_get_list_status_4_success(self):
        """BB 查询协同任务列表，已取消，成功"""
        Log.debug('test_get_list_status_4_success start')
        para_id = 27
        data_id = 27028
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_status_4_success end')
        pass

    def test_get_list_status_5_success(self):
        """BB 查询协同任务列表，被取消，成功"""
        Log.debug('test_get_list_status_5_success start')
        para_id = 27
        data_id = 27029
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_status_5_success end')
        pass

    def test_get_list_status_6_success(self):
        """BB 查询协同任务列表，错误，成功"""
        Log.debug('test_get_list_status_6_success start')
        para_id = 27
        data_id = 27030
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_status_6_success end')
        pass

    def test_get_list_remark_success(self):
        """BB 查询协同任务列表，按备注查询，成功"""
        Log.debug('test_get_list_remark_success start')
        para_id = 27
        data_id = 27031
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_remark_success end')
        pass

    def test_get_list_target_success(self):
        """BB 查询协同任务列表，按计算目标，成功"""
        Log.debug('test_get_list_target_success start')
        para_id = 27
        data_id = 27032
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_target_success end')
        pass

    def test_get_list_mul_1_success(self):
        """BB 查询协同任务列表，布里、gwas、待接收、计算目标联合查询，成功"""
        Log.debug('test_get_list_mul_1_success start')
        para_id = 27
        data_id = 27033
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_mul_1_success end')
        pass

    def test_get_list_mul_2_success(self):
        """BB 查询协同任务列表，香港、vcf、待接收、备注联合查询，成功"""
        Log.debug('test_get_list_mul_2_success start')
        para_id = 27
        data_id = 27034
        res = self.h_t.base_get_list(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                     flag=True)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_mul_2_success end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestGetListBB END BB端')
