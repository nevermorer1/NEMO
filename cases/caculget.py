from common.Base import Base
from cases.login import Login
from common.log import Log
import requests
import json
from common.sql import sql
from common.dataHandle import DataHandle
import random


class CalGet(Base):

    def __init__(self, node=1, path_id=1):
        self.node = node
        Base.__init__(self, node=self.node, path_id=path_id)
        self.node_o = 2 if self.node == 1 else 1
        # self.fh = FileHandle(node=self.node)
        # 本端数据库
        self.con_n = sql(node=self.node)
        # # 对端数据库
        # self.con_o = sql(node=self.node_o)

    def base_get_list_by_accept(self, para_id, data_id, cookies):
        """查询协同计算列表公共方法"""
        # 获取请求url
        url_get_list_by_accept = self.domain + Base.dh.get_path(para_id)
        Log.info('get_list_by_accept request url : {}'.format(url_get_list_by_accept))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 请求数据转换
        if not req_para['calType'] == '':
            req_para['calType'] = eval(req_para['calType'])
        req_para['pageNo'] = eval(req_para['pageNo'])
        req_para['pageSize'] = eval(req_para['pageSize'])
        Log.info('get_list_by_accept request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_get_list_by_accept, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para)).json()
        Log.info('get_list_by_accept response data is {}'.format(res))
        # 结果检查
        actual = self.get_list_by_accept_check(res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_get_detail_by_accept(self, para_id, data_id, cookies):
        """协同计算-查询详情公共方法"""
        # 获取请求url
        url_get_detail_by_accept = self.domain + Base.dh.get_path(para_id)
        Log.info('get_detail_by_accept request url : {}'.format(url_get_detail_by_accept))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 查询数据库taskId，随机选择查询
        req_para['taskId'] = self.get_task_id()
        data_source[0][5] = req_para['taskId']
        Log.info('get_detail_by_accept request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_get_detail_by_accept, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para)).json()
        Log.info('get_detail_by_accept response data is {}'.format(res))
        # 结果检查
        actual = self.get_detail_by_accept_check(req_para['taskId'], res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_get_server(self, para_id, data_id, cookies):
        """协同计算--查询服务器公共方法"""
        # 获取请求url
        url_get_server = self.domain + Base.dh.get_path(para_id)
        Log.info('get_server request url : {}'.format(url_get_server))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        Log.info('get_server request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_get_server, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para)).json()
        Log.info('get_server response data is {}'.format(res))
        # 结果检查
        actual = self.get_server_check(res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def get_server_check(self, res):
        code = '00000'
        if res["code"] != code:
            Log.error('请求返回有误 {}'.format(res))
            return 0
        # 查询数据库服务器列表
        sql_get_server = 'select id serverId,serverName name from t_server order by id'
        data_database = self.con_n.select_dic(sql_get_server)
        Log.info('数据库服务器列表：{}'.format(data_database))
        # 按id升序排列
        data_res = sorted(res['data'], key=lambda k: k['serverId'])
        Log.info('接口查询服务器列表：{}'.format(data_res))
        if len(data_database) == len(data_res):
            Log.info('check success,result is 1')
            return 1
        Log.error('接口返回数据与数据库查询不一致!')
        return 0

    def get_task_id(self):
        """获取task id.返回随机id"""
        sql_task_id = 'select id from t_task'
        res = self.con_n.select(sql_task_id)
        return random.choice(res)[0]

    def get_detail_by_accept_check(self, taskId, res):
        """1 成功 0 失败"""
        code = '00000'
        if res["code"] != code:
            Log.error('返回错误：{}'.format(res))
            return 0
        sql_task = 'select * from t_task where id = %d' % taskId
        data_database = self.con_n.select_dic_single(sql_task)
        data_res = res['data']
        if self.compare(data_database, data_res):
            Log.info('data equal, compare success')
            return 1
        Log.error('data different, compare fail')
        return 0

    @staticmethod
    def compare(data_database, data_res):
        list1 = []
        list2 = []
        list1.append(data_database['id'])
        list2.append(data_res['taskId'])
        list1.append(data_database['calType'])
        list2.append(data_res['calType'])
        list1.append(data_database['startName'])
        list2.append(data_res['startName'])
        list1.append(data_database['startTaskId'])
        list2.append(data_res['startTaskId'])
        list1.append(data_database['remark'])
        list2.append(data_res['remark'])
        list1.append(data_database['status'])
        list2.append(data_res['status'])
        list1.append(data_database['top'])
        list2.append(data_res['top'])
        # list1.append(data_database['logicType'])
        # list2.append(data_res['logicType'])
        Log.info('compare data is database :{}'.format(list1))
        Log.info('compare data is interface :{}'.format(list2))
        if list1 == list2:
            return True
        return False

    @staticmethod
    def get_list_by_accept_check(res):
        code = '00000'
        message = '成功'
        if res['code'] == code and res['message'] == message:
            Log.info('actual res check is 1 ,success !')
            return 1
        Log.error('请求返回有误！{}'.format(res))
        return 0


if __name__ == '__main__':
    Log.debug('*' * 50)
    cv = CalGet(node=1)
    ck = Login(node=1)
    cookie = ck.get_cookie()
    # cookie =None
    para_id = 20
    data_id = 20001
    cv.base_get_server(para_id, data_id, cookie)
    Log.debug('*' * 50)
