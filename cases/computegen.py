from common.Base import Base
from cases.login import Login
from common.log import Log
import requests
import json
import random
from common.sql import sql
from common.dataHandle import DataHandle
from cases.filehandle import FileHandle


class ComputeGen(Base):

    def __init__(self, node=1, path_id=1):
        self.node = node
        Base.__init__(self, node=self.node, path_id=path_id)
        self.node_o = 2 if self.node == 1 else 1
        # 文件上传接口para id
        self.upload_para_id = 10
        # gen 文件类型 2
        self.fileType = 2

        self.fh = FileHandle(node=self.node)
        # 本端数据库
        self.con_n = sql(node=self.node)
        # 对端数据库
        self.con_o = sql(node=self.node_o)

    def base_compute_gen(self, para_id, data_id, cookies, calType=2, max_server=0):
        """gen协同计算  calType:1 随机查找vcf task ; 2 查找基因协同计算任务 3 GWAS 0 查找最大id+6666"""
        # 获取请求url
        url_compute_gen = self.domain + Base.dh.get_path(para_id)
        Log.info('compute_gen request url : {}'.format(url_compute_gen))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 获取task_id
        if not calType:
            req_para['taskId'] = self.get_max_task_id()
        else:
            req_para['taskId'] = self.get_task_id(calType)
        # 获取serverId
        if max_server:
            req_para['serverId'] = self.get_max_server_id()
        else:
            req_para['serverId'] = self.get_server_id()

        # 实际请求参数设置
        data_source[0][5] = req_para['taskId']
        data_source[0][6] = req_para['serverId']
        Log.info('compute_gen request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_compute_gen, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para)).json()
        Log.info('compute_gen response data is {}'.format(res))
        # 结果检查
        actual = self.gen_check(res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def gen_check(self, res):
        code = '00000'
        if res['code'] == code:
            Log.info('result check success ')
            return 1
            # taskId = res['data']
            # Log.debug('taskId is {}'.format(taskId))
            # [data_n, data_o] = self.get_data(taskId)
            # Log.info('本端数据为： {}'.format(data_n))
            # Log.info('对端数据为： {}'.format(data_o))
            # if self.compare(data_n, data_o):
            #     Log.info('compare result is True ,success !')
            #     return 1
            # else:
            #     Log.error('compare result is False ,fail !')
            #     return 0
        Log.error('请求返回有误！{}'.format(res))
        return 0

    def compare(self, data_n, data_o):
        list1 = []
        list2 = []
        list1.append(data_n['calType'])
        list2.append(data_o['calType'])
        list1.append(data_n['startName'])
        list2.append(data_o['startName'])
        list1.append(data_n['acceptName'])
        list2.append(data_o['acceptName'])
        list1.append(data_n['remark'])
        list2.append(data_o['remark'])
        list1.append(data_n['status'])
        list2.append(data_o['status'])
        list1.append(data_n['name'])
        list2.append(data_o['name'])
        Log.info('compare data is {}'.format(list1))
        Log.info('compare data is {}'.format(list2))
        if list1 == list2:
            return True
        return False

    def get_data(self, taskId):
        '根据发起taskid查询两端数据库数据'
        # 本端查询sql
        sql_n = 'select * from t_task_history where id = %d' % taskId
        # 对端查询sql
        sql_o = 'select * from t_task where startTaskId = %d' % taskId
        return [self.con_n.select_dic_single(sql=sql_n),
                self.con_o.select_dic_single(sql=sql_o)]

    def get_max_task_id(self):
        """生成不存在的taskId"""
        sql_max = 'SELECT max(id) from t_task'
        return self.con_n.select_single(sql_max) + 6666

    def get_task_id(self,calType):
        """获取task id.返回随机id"""
        sql_task_id = 'SELECT id from t_task WHERE calType =%d and status =1' % calType
        res = self.con_n.select(sql_task_id)
        task_id = random.choice(res)[0]
        sql_temp = 'SELECT * from t_task WHERE id =%d' % task_id
        task_info = self.con_n.select_dic_single(sql_temp)
        Log.debug('task info is : {}'.format(task_info))
        return task_id

    def get_server_id(self):
        """获取server id.返回随机id"""
        sql_task_id = 'SELECT id from t_server'
        res = self.con_n.select(sql_task_id)
        sever_id = random.choice(res)[0]
        return sever_id

    def get_max_server_id(self):
        """生成不存在的serverId"""
        sql_max = 'SELECT max(id) from t_server'
        return self.con_n.select_single(sql_max) + 6666


if __name__ == '__main__':
    Log.debug('*' * 50)
    cv = ComputeGen(node=1)
    ck = Login(node=1)
    cookie = ck.get_cookie()
    para_id = 23
    data_id = 23001
    cv.base_compute_gen(para_id, data_id, cookie)
    Log.debug('*' * 50)
