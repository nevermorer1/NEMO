from dataHandle import DataHandle
import unittest
from log import Log
from login import Login
from userinfo import UserInfo
import requests
import json
from Base import Base


class TestUserInfoHK(unittest.TestCase):
    """用户相关-HK端"""

    bf = '1c18dc8afa0363def9fe4977dfff2f73'  # 123456入库
    af = '37b1a09078cf51963f48b478ab6efdf9'  # 111111入库

    @classmethod
    def setUpClass(cls):
        Log.info('TestUserInfoHK START HK端')
        # cls.lc = LoadConfig()
        # cls.domain = cls.lc.get_domain()
        cls.node = 1
        cls.dh = DataHandle()
        # 布里端
        cls.L = Login(node=cls.node)
        cls.cookies = cls.L.get_cookie()
        cls.ui = UserInfo(node=cls.node)
        # cls.url = cls.lc.get_domain() + cls.dh.get_path(1)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_insert_user_success(self):
        """HK端新增本端用户成功"""
        data_id = 9001
        para_id = 9
        self.base_insert_user(para_id=para_id, data_id=data_id, cookies=self.cookies)
        Log.debug('test_insert_user_success end')

    def test_insert_user_fail(self):
        """HK端新增对端用户失败"""
        data_id = 9002
        para_id = 9
        self.base_insert_user(para_id=para_id, data_id=data_id, cookies=self.cookies)
        Log.debug('test_insert_user_fail end')

    def test_insert_user_no_session(self):
        """HK端非登录态新增用户"""
        data_id = 9003
        para_id = 9
        self.base_insert_user(para_id=para_id, data_id=data_id, cookies=None)
        Log.debug('test_insert_user_no_session end')

    def base_insert_user(self, para_id, data_id, cookies):
        """新增用户"""
        # 获取请求url
        url_insert = self.ui.domain + Base.dh.get_path(para_id)
        Log.info('insert user request url : {}'.format(url_insert))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 随机生成用户名
        req_para['loginName'] = self.ui.gene_username()
        data_source[0][5] = req_para['loginName']
        req_para['name'] = self.ui.gene_username()
        data_source[0][6] = req_para['name']
        # 接口数据类型转换
        req_para['group'] = eval(req_para['group'])
        req_para['status'] = eval(req_para['status'])
        Log.info('insert user request data is {}'.format(json.dumps(req_para)))
        # 请求接口
        res = requests.post(url=url_insert, headers=Base.headers, cookies=cookies,
                            data=json.dumps(req_para)).json()
        Log.info('insert user response data is {}'.format(res))
        # 结果检查
        actual = self.ui.check(res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 断言结果检查
        self.assertTrue(self.dh.check_result(data_source), msg='result check fail')

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestUserInfoHK END HK端')
