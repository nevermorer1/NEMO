from common.Base import Base
from cases.login import Login
from common.log import Log
import requests
from common.sql import sql
from common.dataHandle import DataHandle
import random


class HistoryTest(Base):

    def __init__(self, node=1, path_id=1):
        self.node = node
        Base.__init__(self, node=self.node, path_id=path_id)
        self.node_o = 2 if self.node == 1 else 1
        # self.fh = FileHandle(node=self.node)
        # 本端数据库
        self.con_n = sql(node=self.node)
        # # 对端数据库
        # self.con_o = sql(node=self.node_o)

    def base_get_list(self, para_id, data_id, cookies, flag):
        """历史记录--查询协同计算列表公共方法"""
        # 获取请求url
        url_get_list_by_accept = self.domain + Base.dh.get_path(para_id)
        Log.info('get_list request url : {}'.format(url_get_list_by_accept))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 请求数据转换
        for key in req_para.keys():
            if key == 'remark' or key == 'target':
                pass
            elif req_para[key] == '':
                pass
            else:
                req_para[key] = eval(req_para[key])
        Log.info('get_list request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_get_list_by_accept, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para)).json()
        Log.info('get_list response data is {}'.format(res))
        # 结果检查
        actual = self.get_list_check(res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_get_detail(self, para_id, data_id, cookies, flag):
        """历史记录-查询详情公共方法"""
        # 获取请求url
        url_get_detail_by_accept = self.domain + Base.dh.get_path(para_id)
        Log.info('get_detail request url : {}'.format(url_get_detail_by_accept))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 查询数据库taskId，随机选择查询
        req_para['taskId'] = self.get_random_task_id()
        data_source[0][5] = req_para['taskId']
        Log.info('get_detail request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_get_detail_by_accept, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para)).json()
        Log.info('get_detail response data is {}'.format(res))
        # 结果检查
        actual = self.get_detail_check(req_para['taskId'], res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_query_update_flag(self, para_id, data_id, cookies, flag):
        """历史记录-数据更新"""
        # 获取请求url
        url_query = self.domain + Base.dh.get_path(para_id)
        Log.info('query request url : {}'.format(url_query))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        Log.info('query request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_query, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para)).json()
        Log.info('query response data is {}'.format(res))
        # 结果检查
        actual = self.get_list_check(res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_logic_get_list(self, para_id, data_id, cookies, flag):
        """逻辑管理-查询列表"""
        # 获取请求url
        url_query = self.domain + Base.dh.get_path(para_id)
        Log.info('logic_get_list request url : {}'.format(url_query))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        Log.info('logic_get_list request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_query, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para)).json()
        Log.info('logic_get_list response data is {}'.format(res))
        # 结果检查
        actual = self.get_logic_check(res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def get_random_task_id(self):
        """获取随机task id.返回随机id"""
        sql_task_id = 'select id from t_task_history'
        res = self.con_n.select(sql_task_id)
        return random.choice(res)[0]

    def get_detail_check(self, taskId, res):
        """1 成功 0 失败"""
        code = '00000'
        if res["code"] != code:
            Log.error('返回错误：{}'.format(res))
            return 0
        sql_task = 'select * from t_task_history where id = %d' % taskId
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
        list1.append(data_database['logicType'])
        list2.append(data_res['logicType'])
        Log.info('compare data is database :{}'.format(list1))
        Log.info('compare data is interface :{}'.format(list2))
        if list1 == list2:
            return True
        return False

    @staticmethod
    def get_list_check(res, flag):
        code = '00000'
        message = '成功'
        if flag and res['code'] != code:
            Log.error('请求返回应该为成功，实际失败 {}'.format(res))
            return 0
        if not flag and res['code'] == code:
            Log.error('异常用例请求返回应该为失败，实际成功 {}'.format(res))
            return 1
        if res['code'] == code and res['message'] == message:
            Log.info('actual res check is 1 ,success !')
            return 1
        Log.error('请求返回有误！{}'.format(res))
        return 0

    def get_logic_check(self, res, flag):
        code = '00000'
        if flag and res['code'] != code:
            Log.error('请求返回应该为成功，实际失败 {}'.format(res))
            return 0
        if not flag and res['code'] == code:
            Log.error('异常用例请求返回应该为失败，实际成功 {}'.format(res))
            return 1
        if res["code"] != code:
            Log.error('请求返回有误 {}'.format(res))
            return 0
        # 查询数据库服务器列表
        sql_get_logic = 'select * from t_logic order by id'
        data_database = self.con_n.select_dic(sql_get_logic)
        # 列表中的字典元素按key排序
        for i in range(len(data_database)):
            data_database[i] = Base.order_dic_by_keys(data_database[i])
        Log.info('数据库t_logic列表排序后：{}'.format(data_database))
        # 列表元素按id升序排列
        data_res = sorted(res['data'], key=lambda k: k['id'])
        # 列表中的字典元素按key排序
        for i in range(len(data_res)):
            data_res[i] = Base.order_dic_by_keys(data_res[i])
        Log.info('接口查询logic列表排序后：{}'.format(data_res))
        if data_database == data_res:
            Log.info('check success,result is 1')
            return 1
        Log.error('接口返回数据与数据库查询不一致!')
        return 0


if __name__ == '__main__':
    Log.debug('*' * 50)
    cv = HistoryTest(node=1)
    ck = Login(node=1)
    cookie = ck.get_cookie()
    # cookie =None
    para_id = 27
    data_id = 27001
    cv.base_get_list(para_id, data_id, cookie, flag=True)
    Log.debug('*' * 50)
