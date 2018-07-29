from common.Base import Base
from cases.login import Login
from common.log import Log
import requests
import json
from common.sql import sql
from common.dataHandle import DataHandle


class UserInfo(Base):
    bf = '1c18dc8afa0363def9fe4977dfff2f73'  # 123456入库
    af = '37b1a09078cf51963f48b478ab6efdf9'  # 111111入库

    def __init__(self, node=1, path_id=1):
        """ @:param node  1: hongkong other:bulisiban
            @:param p_id  path id
        """
        # self.cookies = Login(node=node, path_id=1).get_cookie()
        self.s = sql(node=node)
        Base.__init__(self, node=node, path_id=path_id)
        pass

    def base_reset_password(self, para_id, data_id, cookies):
        """admin重置用户密码"""
        # 获取请求url
        url_reset = self.domain + Base.dh.get_path(para_id)
        Log.info('reset_password url is {}'.format(url_reset))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        sql = 'SELECT id FROM t_user WHERE loginName = \'Automation\''
        # 设置 userid
        req_para['userId'] = self.s.select_single(sql)
        data_source[0][5] = req_para['userId']
        Log.info('reset_password data is {}'.format(req_para))
        # 请求前数据库检查
        self.before_reset()
        # 请求接口
        res = requests.post(url=url_reset, headers=Base.headers, cookies=cookies,
                            data=json.dumps(req_para)).json()
        Log.info('reset_password response data is {}'.format(res))
        # 结果检查
        actual = self.after_reset_check(res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_insert_user(self, para_id, data_id, cookies):
        """新增用户公共方法"""
        # 获取请求url
        url_insert = self.domain + Base.dh.get_path(para_id)
        Log.info('insert user request url : {}'.format(url_insert))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 随机生成用户名
        req_para['loginName'] = self.gene_username()
        data_source[0][5] = req_para['loginName']
        req_para['name'] = self.gene_username()
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
        actual = self.check(res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_modify_password(self, para_id, data_id, cookies):
        """用户修改密码公共方法"""
        # 获取请求url
        url_modify = self.domain + Base.dh.get_path(para_id)
        Log.info('insert user request url : {}'.format(url_modify))
        # 获取请求数据，md5
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        req_para['userId'] = self.get_user_id()
        data_source[0][5] = req_para['userId']
        req_para['password'] = Base.make_password(req_para['password'])
        req_para['newPassword'] = Base.make_password(req_para['newPassword'])
        Log.info('modify_password data is {}'.format(req_para))
        # 请求前数据库检查
        self.before_modify_check()
        # 请求
        res = requests.post(url=url_modify, headers=Base.headers, cookies=cookies,
                            data=json.dumps(req_para)).json()
        Log.info('modify_password response data is {}'.format(res))
        # 结果检查
        actual = self.modify_check(res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_get_list_by_condition(self, para_id, data_id, cookies):
        """获取用户列表"""
        # 获取请求url
        url_get_list_by_condition = self.domain + Base.dh.get_path(para_id)
        Log.info('get_list_by_condition request url : {}'.format(url_get_list_by_condition))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        Log.info('get_list_by_condition request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_get_list_by_condition, headers=Base.headers, cookies=cookies,
                            data=json.dumps(req_para)).json()
        Log.info('get_list_by_condition response data is {}'.format(res))
        # 结果检查
        actual = self.check(res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_get_user_by_id(self, para_id, data_id, cookies):
        """查询用户详情"""
        # 获取请求url
        url_get_user_by_id = self.domain + Base.dh.get_path(para_id)
        Log.info('get_user_by_id request url : {}'.format(url_get_user_by_id))

        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        sql = 'SELECT id FROM t_user WHERE loginName = \'Automation\''
        # 设置 userid
        req_para['userId'] = self.s.select_single(sql)
        data_source[0][5] = req_para['userId']
        Log.info('get_user_by_id request data : {}'.format(req_para))
        # 请求
        res = requests.post(url=url_get_user_by_id, headers=Base.headers, cookies=cookies,
                            data=json.dumps(req_para)).json()
        Log.info('get_user_by_id response data is {}'.format(res))
        # 结果检查
        actual = self.check(res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def before_reset(self):
        """重置用户密码前数据验证"""
        sql_select = 'SELECT password FROM t_user WHERE loginName = \'Automation\''
        sql_update = "UPDATE t_user SET `password`= '%s' WHERE loginName=\'Automation\'" \
                     % self.af
        if self.bf != self.s.select_single(sql_select):
            Log.debug("重置密码前，数据库密码非原始密码123456，不需修改")
            pass
        else:
            self.s.updata(sql_update)
            Log.debug("重置密码前，数据库密码为原始密码123456，更改为111111")
        pass

    def after_reset_check(self, res):
        """ 修改密码结果验证，检查请求返回值和数据库
         1 成功 0 失败"""
        sql_select = 'SELECT password FROM t_user WHERE loginName = \'Automation\''
        code = '00000'
        msg = "成功"

        if res["code"] == code and res["message"] == msg \
                and self.bf == self.s.select_single(sql_select):
            Log.debug('actual res check is 1')
            return 1
        else:
            Log.debug('actual res check is 0')
            return 0

    def before_modify_check(self):
        """用户修改密码前数据验证"""
        sql_select = 'SELECT password FROM t_user WHERE loginName = \'Automation\''
        sql_update = "UPDATE t_user SET `password`= '%s' WHERE loginName=\'Automation\'" \
                     % self.bf

        if self.bf == self.s.select_single(sql_select):
            Log.debug("当前数据库密码为123456，不需修改")
            pass
        else:
            self.s.updata(sql_update)
            Log.debug("当前数据库密码不是123456，更改为123456")

    def modify_check(self, res):
        """ 修改密码结果验证，检查请求返回值和数据库
         1 成功 0 失败"""
        sql_select = 'SELECT password FROM t_user WHERE loginName = \'Automation\''
        code = '00000'
        msg = "成功"

        if res["code"] == code and res["message"] == msg \
                and self.af == self.s.select_single(sql_select):
            Log.debug('actual res check is 1')
            return 1
        else:
            Log.debug('actual res check is 0')
            return 0

    def get_user_id(self):
        """获取Automation user_id"""
        sql = 'SELECT id FROM t_user WHERE loginName = \'Automation\''
        return self.s.select(sql)[0][0]

    def modify_cookies(self, data_id, node):
        """获取automation登录后cookie"""
        self.before_modify_check()
        L = Login(node=node)
        cookie_modify = L.get_cookie(data_id=data_id)
        return cookie_modify

    @staticmethod
    def check(res):
        """1 成功 0 失败"""
        code = '00000'
        msg = "成功"
        if res["code"] == code and res["message"] == msg:
            Log.debug('actual res check is 1')
            return 1
        else:
            Log.debug('actual res check is 0')
            return 0


if __name__ == '__main__':
    # para1_id = 5
    # data1_id = 5001
    UI = UserInfo(node=1, path_id=1)
    # cookies = UI.cookies
    # print(UI.reset_password(para_id=para1_id, data_id=data1_id,
    #                         cookies=cookies).json())
