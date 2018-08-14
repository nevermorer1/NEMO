from common.Base import Base
from cases.login import Login
from common.log import Log
import requests
from common.sql import sql
from common.dataHandle import DataHandle
import time


class CancelTask(Base):

    def __init__(self, node=1, path_id=1):
        self.node = node
        Base.__init__(self, node=self.node, path_id=path_id)
        self.node_o = 2 if self.node == 1 else 1

        # 本端数据库
        self.con_n = sql(node=self.node)
        # 对端数据库
        self.con_o = sql(node=self.node_o)

    def base_cancel_task(self, para_id, data_id, cookies, flag, task_modify=0, reason_modify=0):
        """协同计算--取消任务"""
        # 获取请求url
        url_vcf_start = self.domain + Base.dh.get_path(para_id)
        Log.info('cancel_task request url : {}'.format(url_vcf_start))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)

        req_para['type'] = eval(req_para['type'])

        # 不存在的taskId
        if task_modify:
            temp = {'taskId': None, 'startTaskId': None}
            req_para['taskId'] = self.get_max_task_id(req_para['type'])
        else:
            # 获取请求参数,temp存储id,startTaskId组成的字典
            temp = self.get_task_id(req_para['type'])
            req_para['taskId'] = temp['id']

        # reason 内容
        if reason_modify:
            req_para['reason'] = req_para['reason'] * 100

        data_source[0][5] = req_para['taskId']
        data_source[0][7] = req_para['reason']
        Log.info('cancel_task request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_vcf_start, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para)).json()
        Log.info('cancel_task response data is {}'.format(res))
        # 结果检查
        actual = self.cancel_check(res, temp, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_query_update_flag(self, para_id, data_id, cookies, flag):
        """协同计算--数据更新"""
        # 获取请求url
        url_query_update_flag = self.domain + Base.dh.get_path(para_id)
        Log.info('query_update_flag request url : {}'.format(url_query_update_flag))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)

        Log.info('query_update_flag request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_query_update_flag, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para)).json()
        Log.info('query_update_flag response data is {}'.format(res))
        # 结果检查
        actual = self.query_check(res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def query_check(self, res, flag):
        code = '00000'
        if flag and res['code'] != code:
            Log.error('请求返回应该为成功，实际失败 {}'.format(res))
            return 0
        if not flag and res['code'] == code:
            Log.error('异常用例请求返回应该为失败，实际成功 {}'.format(res))
            return 1
        if not res['code'] == code:
            Log.error('请求返回有误！{}'.format(res))
            return 0
        else:
            Log.info('check success')
            return 1

    def get_task_id(self, ctype):
        """查询id、startTaskId,返回字典"""
        table = 't_task' if ctype == 1 else 't_task_history'
        sql_m = 'select id,startTaskId from %s where status = 1 order by id desc' % table
        Log.info(sql_m)
        result = self.con_n.select_dic(sql_m)
        Log.debug('数据库查询数据为：{}'.format(result))
        res = result[0]
        # res = random.choice(result)
        Log.info('id,startTaskId is :{}'.format(res))
        return res

    def cancel_check(self, res, temp, flag):
        code = '00000'
        if flag and res['code'] != code:
            raise AssertionError('请求返回应该为成功，实际失败 {}'.format(res))
        if not flag and res['code'] == code:
            raise AssertionError('异常用例请求返回应该为失败，实际成功 {}'.format(res))
        if not res['code'] == code:
            Log.error('请求返回有误！{}'.format(res))
            return 0
        else:
            if temp['startTaskId'] is None:
                status = 4
                id = temp['id']
                sql_n = 'select * from t_task_history where id = %d ' % id
                sql_o = 'select * from t_task_history where startTaskId = %d ' % id
            else:
                status = 5
                id = temp['startTaskId']
                sql_n = 'select * from t_task_history where startTaskId = %d ' % id
                sql_o = 'select * from t_task_history where id = %d ' % id
            Log.debug('本端查询sql：{}'.format(sql_n))
            Log.debug('对端查询sql：{}'.format(sql_o))
            data_n = self.con_n.select_dic_single(sql=sql_n)
            Log.info('本端数据为： {}'.format(data_n))
            time.sleep(10)
            try:
                data_o = self.con_o.select_dic_single(sql=sql_o)
            except IndexError as e:
                raise AssertionError('数据库查询为空，exception is:{}'.format(e))
            Log.info('对端数据为： {}'.format(data_o))

            if self.compare(data_n, data_o, status):
                Log.info('compare result is True ,success !')
                return 1
            else:
                Log.error('compare result is False ,fail !')
                return 0

    def compare(self, data_n, data_o, status):
        list1 = []
        list2 = []
        list1.append(data_n['status'])
        list2.append(data_o['status'])
        list1.append(data_n['name'])
        list2.append(data_o['name'])
        list1.append(data_n['calType'])
        list2.append(data_o['calType'])
        # list1.append(data_n['logicType'])
        # list2.append(data_o['logicType'])
        list1.append(data_n['top'])
        list2.append(data_o['top'])
        list1.append(data_n['startName'])
        list2.append(data_o['startName'])
        list1.append(data_n['acceptName'])
        list2.append(data_o['acceptName'])
        list1.append(data_n['remark'])
        list2.append(data_o['remark'])
        list1.append(data_n['reason'])
        list2.append(data_o['reason'])

        Log.info('compare data is {}'.format(list1))
        Log.info('compare data is {}'.format(list2))
        if list1 == list2 and list1[0] == status:
            return True
        return False

    def get_max_task_id(self, ctype):
        table = 't_task' if ctype == 1 else 't_task_history'
        sql_max = 'SELECT max(id) from {}'.format(table)
        return self.con_n.select_single(sql_max) + 6666


if __name__ == '__main__':
    Log.debug('*' * 50)
    cv = CancelTask(node=1)
    # print(cv.get_task_id(2))
    ck = Login(node=1)
    cookie = ck.get_cookie()
    para_id = 21
    data_id = 21001
    cv.base_cancel_task(para_id, data_id, cookie, task_modify=0, reason_modify=0)
    Log.debug('*' * 50)
