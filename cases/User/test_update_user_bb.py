from common.dataHandle import DataHandle
import unittest
from common.log import Log
from cases.login import Login
from cases.userinfo import UserInfo


class TestUpdateUserBB(unittest.TestCase):
    """用户相关(修改用户信息)-BB端"""

    @classmethod
    def setUpClass(cls):
        Log.info('TestUpdateUserBB START BB端')
        cls.node = 2
        cls.dh = DataHandle()
        # 香港端
        cls.L = Login(node=cls.node)
        cls.admin_cookies = cls.L.get_cookie()
        cls.ui = UserInfo(node=cls.node)
        # cls.url = cls.lc.get_domain() + cls.dh.get_path(1)
        # auto登录cookie
        cls.AUTO_cookies = cls.ui.modify_cookies(data_id=3001, node=cls.node)

    def setUp(self):
        Log.debug('---------')
        pass

    def test_update_status_0(self):
        """BB admin  修改用户信息status 0"""
        para_id = 7
        data_id = 7009
        res = self.ui.base_update_user(para_id=para_id, data_id=data_id,
                                       cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_update_status_0 end')

    def test_update_status_1(self):
        """BB admin  修改用户信息status 1"""
        para_id = 7
        data_id = 7010
        res = self.ui.base_update_user(para_id=para_id, data_id=data_id,
                                       cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_update_status_1 end')

    def test_update_status_undefined(self):
        """BB admin  修改用户信息status未定义失败"""
        para_id = 7
        data_id = 7011
        res = self.ui.base_update_user(para_id=para_id, data_id=data_id,
                                       cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_update_status_undefined end')

    def test_update_group_1(self):
        """BB admin  修改用户信息group只能为1，成功"""
        para_id = 7
        data_id = 7012
        res = self.ui.base_update_user(para_id=para_id, data_id=data_id,
                                       cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_update_group_1 end')

    def test_update_group_2(self):
        """BB admin  修改用户信息group 2对端group修改失败"""
        para_id = 7
        data_id = 7013
        res = self.ui.base_update_user(para_id=para_id, data_id=data_id,
                                       cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_update_group_2 end')

    def test_update_group_undefined(self):
        """BB admin  修改用户信息group未定义，修改失败"""
        para_id = 7
        data_id = 7014
        res = self.ui.base_update_user(para_id=para_id, data_id=data_id,
                                       cookies=self.admin_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_update_group_undefined end')

    def test_update_group_no_admin(self):
        """BB 非admin  修改用户信息失败"""
        para_id = 7
        data_id = 7015
        res = self.ui.base_update_user(para_id=para_id, data_id=data_id,
                                       cookies=self.AUTO_cookies)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_update_group_no_admin end')

    def test_update_group_no_session(self):
        """BB 未登录 修改用户信息失败"""
        para_id = 7
        data_id = 7016
        res = self.ui.base_update_user(para_id=para_id, data_id=data_id,
                                       cookies=None)
        self.assertTrue(res, msg='result check fail')
        Log.debug('test_update_group_no_session end')

    def tearDown(self):
        Log.debug('---------')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('TestUpdateUserBB END BB端')
