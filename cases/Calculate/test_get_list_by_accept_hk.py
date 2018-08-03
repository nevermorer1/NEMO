from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.caculget import CalGet


class TestGetListByAcceptHK(unittest.TestCase):
    """查询协同计算列表-HK端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestGetListByAcceptHK START HK端')
        cls.node = 1
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.cal_get = CalGet(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_get_list_by_accept_all_success(self):
        """HK 查询协同计算列表 全部 查询成功"""
        Log.debug('test_get_list_by_accept_all_success start')
        para_id = 18
        data_id = 18001
        res = self.cal_get.base_get_list_by_accept(para_id=para_id, data_id=data_id, cookies=self.admin_cookies, )
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_by_accept_all_success end')
        pass

    def test_get_list_by_accept_no_session_fail(self):
        """HK 查询协同计算列表 全部 未登录，查询失败"""
        Log.debug('test_get_list_by_accept_no_session_fail start')
        para_id = 18
        data_id = 18002
        res = self.cal_get.base_get_list_by_accept(para_id=para_id, data_id=data_id, cookies=None)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_by_accept_no_session_fail end')
        pass

    def test_get_list_by_accept_vcf_success(self):
        """HK 查询协同计算列表 vcf数据集 查询成功"""
        Log.debug('test_get_list_by_accept_vcf_success start')
        para_id = 18
        data_id = 18003
        res = self.cal_get.base_get_list_by_accept(para_id=para_id, data_id=data_id, cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_by_accept_vcf_success end')
        pass

    def test_get_list_by_accept_gen_success(self):
        """HK 查询协同计算列表 基因编辑距离比对 查询成功"""
        Log.debug('test_get_list_by_accept_gen_success start')
        para_id = 18
        data_id = 18004
        res = self.cal_get.base_get_list_by_accept(para_id=para_id, data_id=data_id, cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_by_accept_gen_success end')
        pass

    def test_get_list_by_accept_gwas_success(self):
        """HK 查询协同计算列表 GWAS计算 查询成功"""
        Log.debug('test_get_list_by_accept_gwas_success start')
        para_id = 18
        data_id = 18005
        res = self.cal_get.base_get_list_by_accept(para_id=para_id, data_id=data_id, cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_by_accept_gwas_success end')
        pass

    def test_get_list_by_accept_vcf_remark_success(self):
        """HK 查询协同计算列表 vcf数据集、备注联合查询 查询成功"""
        Log.debug('test_get_list_by_accept_vcf_remark_success start')
        para_id = 18
        data_id = 18006
        res = self.cal_get.base_get_list_by_accept(para_id=para_id, data_id=data_id, cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_by_accept_vcf_remark_success end')
        pass

    def test_get_list_by_accept_vcf_target_success(self):
        """HK 查询协同计算列表 vcf数据集、计算目标联合查询 查询成功"""
        Log.debug('test_get_list_by_accept_vcf_target_success start')
        para_id = 18
        data_id = 18007
        res = self.cal_get.base_get_list_by_accept(para_id=para_id, data_id=data_id, cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_by_accept_vcf_target_success end')
        pass

    def test_get_list_by_accept_gen_remark_success(self):
        """HK 查询协同计算列表 基因编辑距离比对、备注联合查询 查询成功"""
        Log.debug('test_get_list_by_accept_gen_remark_success start')
        para_id = 18
        data_id = 18008
        res = self.cal_get.base_get_list_by_accept(para_id=para_id, data_id=data_id, cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_by_accept_gen_remark_success end')
        pass

    def test_get_list_by_accept_gen_target_success(self):
        """HK 查询协同计算列表 基因编辑距离比对、计算目标联合查询 查询成功"""
        Log.debug('test_get_list_by_accept_gen_target_success start')
        para_id = 18
        data_id = 18009
        res = self.cal_get.base_get_list_by_accept(para_id=para_id, data_id=data_id, cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_by_accept_gen_target_success end')
        pass

    def test_get_list_by_accept_gwas_remark_success(self):
        """HK 查询协同计算列表 GWAS计算、备注联合查询 查询成功"""
        Log.debug('test_get_list_by_accept_gwas_remark_success start')
        para_id = 18
        data_id = 18010
        res = self.cal_get.base_get_list_by_accept(para_id=para_id, data_id=data_id, cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_by_accept_gwas_remark_success end')
        pass

    def test_get_list_by_accept_gwas_target_success(self):
        """HK 查询协同计算列表 GWAS计算、计算目标联合查询 查询成功"""
        Log.debug('test_get_list_by_accept_gwas_target_success start')
        para_id = 18
        data_id = 18011
        res = self.cal_get.base_get_list_by_accept(para_id=para_id, data_id=data_id, cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_by_accept_gwas_target_success end')
        pass

    def test_get_list_by_accept_all_remark_success(self):
        """HK 查询协同计算列表 全部、备注联合查询 查询成功"""
        Log.debug('test_get_list_by_accept_all_remark_success start')
        para_id = 18
        data_id = 18012
        res = self.cal_get.base_get_list_by_accept(para_id=para_id, data_id=data_id, cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_by_accept_all_remark_success end')
        pass

    def test_get_list_by_accept_all_target_success(self):
        """HK 查询协同计算列表 全部、计算目标联合查询 查询成功"""
        Log.debug('test_get_list_by_accept_all_target_success start')
        para_id = 18
        data_id = 18013
        res = self.cal_get.base_get_list_by_accept(para_id=para_id, data_id=data_id, cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_get_list_by_accept_all_target_success end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestGetListByAcceptHK END HK端')
