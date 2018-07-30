from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.userinfo import UserInfo


class TestUserInfoBB(unittest.TestCase):
    """用户相关(新增用户、用户修改密码、重置密码等)-BB端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestUserInfoBB START BB端')
        # cls.lc = LoadConfig()
        # cls.domain = cls.lc.get_domain()
        cls.node = 2
        cls.dh = DataHandle()
        # 布里端
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
        """BB端新增本端用户成功"""
        data_id = 9004
        para_id = 9
        res = self.ui.base_insert_user(para_id=para_id, data_id=data_id,
                                       cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_insert_user_success end')

    def test_insert_user_fail(self):
        """BB端新增对端用户失败"""
        data_id = 9005
        para_id = 9
        res = self.ui.base_insert_user(para_id=para_id, data_id=data_id,
                                         cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_insert_user_fail end')

    def test_insert_user_no_session(self):
        """BB端非登录态新增用户失败"""
        data_id = 9006
        para_id = 9
        res = self.ui.base_insert_user(para_id=para_id, data_id=data_id,
                                       cookies=None)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_insert_user_no_session end')

    def test_modify_password_success(self):
        """用户修改密码成功"""
        para_id = 3
        data_id = 3005
        res = self.ui.base_modify_password(para_id=para_id, data_id=data_id,
                                           cookies=self.modify_cookie)
        self.assertTrue(res, msg='result check fail')

    def test_modify_password_fail(self):
        """原密码错误，用户修改密码失败"""
        para_id = 3
        data_id = 3006
        # 接口稳定后需细化errcode或者errmessage，防止用例假成功
        res = self.ui.base_modify_password(para_id=para_id, data_id=data_id,
                                           cookies=self.modify_cookie)
        self.assertTrue(res, msg='result check fail')

    def test_modify_password_fail_no_session(self):
        """未登录，用户修改密码失败"""
        para_id = 3
        data_id = 3007
        res = self.ui.base_modify_password(para_id=para_id, data_id=data_id,
                                           cookies=None)
        self.assertTrue(res, msg='result check fail')

    def test_reset_password_success(self):
        """admin重置用户密码成功"""
        para_id = 5
        data_id = 5004
        res = self.ui.base_reset_password(para_id=para_id, data_id=data_id,
                                          cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')

    def test_reset_password_fail_no_session(self):
        """未登录，重置用户密码失败"""
        para_id = 5
        data_id = 5005
        res = self.ui.base_reset_password(para_id=para_id, data_id=data_id,
                                          cookies=None)
        self.assertTrue(res, msg='result check fail')

    def test_reset_password_fail_no_admin(self):
        """非admin，重置用户密码失败"""
        para_id = 5
        data_id = 5006
        res = self.ui.base_reset_password(para_id=para_id, data_id=data_id,
                                          cookies=self.modify_cookie)
        self.assertTrue(res, msg='result check fail')

    def test_get_list_by_condition_success(self):
        """BB admin  查询用户列表成功"""
        para_id = 6
        data_id = 6004
        res = self.ui.base_get_list_by_condition(para_id=para_id, data_id=data_id,
                                                 cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')

    def test_get_list_by_condition_no_admin_fail(self):
        """BB 非admin  查询用户列表失败"""
        para_id = 6
        data_id = 6005
        res = self.ui.base_get_list_by_condition(para_id=para_id, data_id=data_id,
                                                 cookies=self.modify_cookie)
        self.assertTrue(res, msg='result check fail')

    def test_get_list_by_condition_no_session_fail(self):
        """BB 未登录  查询用户列表失败"""
        para_id = 6
        data_id = 6006
        res = self.ui.base_get_list_by_condition(para_id=para_id, data_id=data_id,
                                                 cookies=None)
        self.assertTrue(res, msg='result check fail')

    def test_get_user_by_id_success(self):
        """BB admin  查询用户详情成功"""
        para_id = 8
        data_id = 8004
        res = self.ui.base_get_user_by_id(para_id=para_id, data_id=data_id,
                                          cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')

    def test_get_user_by_id_no_admin_fail(self):
        """BB 非admin  查询用户详情失败"""
        para_id = 8
        data_id = 8005
        res = self.ui.base_get_user_by_id(para_id=para_id, data_id=data_id,
                                          cookies=self.modify_cookie)
        self.assertTrue(res, msg='result check fail')

    def test_get_user_by_id_no_session_fail(self):
        """BB 未登录  查询用户详情失败"""
        para_id = 8
        data_id = 8006
        res = self.ui.base_get_user_by_id(para_id=para_id, data_id=data_id,
                                          cookies=None)
        self.assertTrue(res, msg='result check fail')

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestUserInfoBB END BB端')
