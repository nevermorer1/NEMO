from dataHandle import DataHandle
import unittest
from log import Log
from login import Login
from userinfo import UserInfo


class TestUserInfoHK(unittest.TestCase):
    """用户相关(新增用户、用户修改密码、重置密码等)-HK端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestUserInfoHK START HK端')
        # cls.lc = LoadConfig()
        # cls.domain = cls.lc.get_domain()
        cls.node = 1
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.ui = UserInfo(node=cls.node)
        # cls.url = cls.lc.get_domain() + cls.dh.get_path(1)
        # auto登录cookie
        cls.modify_cookie = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_insert_user_success(self):
        """HK端新增本端用户成功"""
        data_id = 9001
        para_id = 9
        res = self.ui.base_insert_user(para_id=para_id, data_id=data_id,
                                       cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_insert_user_success end')

    def test_insert_user_fail(self):
        """HK端新增对端用户失败"""
        data_id = 9002
        para_id = 9
        res = self.ui.base_insert_user(para_id=para_id, data_id=data_id,
                                         cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_insert_user_fail end')

    def test_insert_user_no_session(self):
        """HK端非登录态新增用户失败"""
        data_id = 9003
        para_id = 9
        res = self.ui.base_insert_user(para_id=para_id, data_id=data_id,
                                       cookies=None)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_insert_user_no_session end')

    def test_modify_password_success(self):
        """用户修改密码成功"""
        para_id = 3
        data_id = 3002
        res = self.ui.base_modify_password(para_id=para_id, data_id=data_id,
                                           cookies=self.modify_cookie)
        self.assertTrue(res, msg='result check fail')

    def test_modify_password_fail(self):
        """原密码错误，用户修改密码失败"""
        para_id = 3
        data_id = 3003
        # 接口稳定后需细化errcode或者errmessage，防止用例假成功
        res = self.ui.base_modify_password(para_id=para_id, data_id=data_id,
                                           cookies=self.modify_cookie)
        self.assertTrue(res, msg='result check fail')

    def test_modify_password_fail_no_session(self):
        """未登录，用户修改密码失败"""
        para_id = 3
        data_id = 3004
        res = self.ui.base_modify_password(para_id=para_id, data_id=data_id,
                                           cookies=None)
        self.assertTrue(res, msg='result check fail')

    def test_reset_password_success(self):
        """admin重置用户密码成功"""
        para_id = 5
        data_id = 5001
        res = self.ui.base_reset_password(para_id=para_id, data_id=data_id,
                                          cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')

    def test_reset_password_fail_no_session(self):
        """未登录，重置用户密码失败"""
        para_id = 5
        data_id = 5002
        res = self.ui.base_reset_password(para_id=para_id, data_id=data_id,
                                          cookies=None)
        self.assertTrue(res, msg='result check fail')

    def test_reset_password_fail_no_admin(self):
        """非admin，重置用户密码失败"""
        para_id = 5
        data_id = 5003
        res = self.ui.base_reset_password(para_id=para_id, data_id=data_id,
                                          cookies=self.modify_cookie)
        self.assertTrue(res, msg='result check fail')

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestUserInfoHK END HK端')
