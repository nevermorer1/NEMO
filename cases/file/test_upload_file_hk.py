from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from filehandle import FileHandle


class TestUpLoadFileHK(unittest.TestCase):
    """文件上传-HK端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestUpLoadFileHK START HK端')
        cls.node = 1
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.fh = FileHandle(node=cls.node)
        # auto登录cookie
        # cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_upload_vcf_success(self):
        """HK 文件类型1-vcf文件，上传成功"""
        Log.debug('test_upload_file_success start')
        para_id = 10
        data_id = 10009
        res = self.fh.base_upload(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                  isChange=0, noFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_query_in_status end')
        pass

    def test_upload_gen_success(self):
        """HK 文件类型2-gen文件，上传成功"""
        Log.debug('test_upload_file_success start')
        para_id = 10
        data_id = 10010
        res = self.fh.base_upload(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                  isChange=0, noFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_query_in_status end')
        pass

    def test_upload_gwas_success(self):
        """HK 文件类型3-gwas文件，上传成功"""
        Log.debug('test_upload_file_success start')
        para_id = 10
        data_id = 10011
        res = self.fh.base_upload(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                  isChange=0, noFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_query_in_status end')
        pass

    def test_upload_file_no_session(self):
        """HK 未登录文件上传失败"""
        Log.debug('test_upload_file_success start')
        para_id = 10
        data_id = 10012
        res = self.fh.base_upload(para_id=para_id, data_id=data_id, cookies=None,
                                  isChange=0, noFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_query_in_status end')
        pass

    def test_upload_file_conflict_name(self):
        """HK 文件名称不一致，上传失败"""
        Log.debug('test_upload_file_success start')
        para_id = 10
        data_id = 10013
        res = self.fh.base_upload(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                  isChange=1, noFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_query_in_status end')
        pass

    def test_upload_file_undefined_filetype(self):
        """HK 文件类型非法数字(非1，2，3)，上传失败"""
        Log.debug('test_upload_file_success start')
        para_id = 10
        data_id = 10014
        res = self.fh.base_upload(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                  isChange=0, noFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_query_in_status end')
        pass

    def test_upload_file_no_file(self):
        """HK 文件为空，上传失败"""
        Log.debug('test_upload_file_success start')
        para_id = 10
        data_id = 10015
        res = self.fh.base_upload(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                  isChange=0, noFile=1)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_query_in_status end')
        pass

    def test_upload_file_not_txt(self):
        """HK 非txt文件，上传失败"""
        Log.debug('test_upload_file_success start')
        para_id = 10
        data_id = 10016
        res = self.fh.base_upload(para_id=para_id, data_id=data_id, cookies=self.admin_cookies,
                                  isChange=0, noFile=0)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_query_in_status end')
        pass

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestUpLoadFileHK END HK端')
