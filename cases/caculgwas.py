from common.Base import Base
from cases.login import Login
from common.log import Log
import requests
import json
from common.sql import sql
from common.dataHandle import DataHandle
from cases.filehandle import FileHandle
import time


class CalGwas(Base):

    def __init__(self, node=1, path_id=1):
        self.node = node
        Base.__init__(self, node=self.node, path_id=path_id)
        self.node_o = 2 if self.node == 1 else 1
        # 文件上传接口para id
        self.upload_para_id = 10
        # gwas 文件类型 3
        self.fileType = 3

        self.fh = FileHandle(node=self.node)
        # 本端数据库
        self.con_n = sql(node=self.node)
        # 对端数据库
        self.con_o = sql(node=self.node_o)

    def base_gwas_start(self, para_id, data_id, cookies, isChange=0, maxFile=0):
        """gwas start gwas计算发起. isChange:0读取请求数据，1 请求数据重复100遍"""
        # 获取请求url
        url_gwas_start = self.domain + Base.dh.get_path(para_id)
        Log.info('gwas_start request url : {}'.format(url_gwas_start))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 登录态判断
        if cookies is not None:
            # 不存在的fileid
            if maxFile:
                req_para['fileList'] = self.get_max_file_id()
                data_source[0][5] = req_para['fileList']
            else:
                # fileList 字符串转列表
                req_para['fileList'] = eval(req_para['fileList'])
                # fileList 文件上传，获取文件id,如果文件列表为空，则跳过上传文件操作
                if len(req_para['fileList']) > 0:
                    req_para['fileList'] = self.gene_file_id_list(req_para['fileList'], cookies)
                    data_source[0][5] = req_para['fileList']
                else:
                    pass
        # remark 内容
        if isChange:
            req_para['remark'] = req_para['remark'] * 100
            data_source[0][7] = req_para['remark']

        # logicType 数据转换
        req_para['logicType'] = eval(req_para['logicType'])
        req_para['isPrint'] = eval(req_para['isPrint'])
        Log.info('gwas_start request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_gwas_start, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para)).json()
        Log.info('gwas_start response data is {}'.format(res))
        # 结果检查
        actual = self.gwas_check(res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_gwas_status(self, para_id, data_id, cookies):
        """gwas start gwas计算发起. 状态测试"""
        # 获取请求url
        url_gwas_start = self.domain + Base.dh.get_path(para_id)
        Log.info('gwas_start request url : {}'.format(url_gwas_start))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)

        req_para['fileList'] = eval(req_para['fileList'])
        # fileList 文件上传，获取文件id
        req_para['fileList'] = self.gene_file_id_list(req_para['fileList'], cookies)
        data_source[0][5] = req_para['fileList']

        # logicType 数据转换
        req_para['logicType'] = eval(req_para['logicType'])
        req_para['isPrint'] = eval(req_para['isPrint'])
        Log.info('gwas_start request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_gwas_start, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para)).json()
        Log.info('gwas_start response data is {}'.format(res))
        # 结果检查
        status = eval(data_source[0][3])
        actual = self.gwas_check_status(res, status)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def gwas_check_status(self, res, status):
        code = '00000'

        if res['code'] == code:
            taskId = res['data']
            Log.debug('taskId is {}'.format(taskId))
            time.sleep(5)
            if status == 1:
                [data_n, data_o] = self.get_data(taskId)
            else:
                [data_n, data_o] = self.get_data_history(taskId)
            Log.info('本端状态为： {}'.format(data_n['status']))
            Log.info('对端状态为： {}'.format(data_o['status']))
            Log.info('期望状态为：{}'.format(status))
            if data_n['status'] == data_o['status'] and data_n['status'] == status:
                Log.info('双端状态与期望状态一致，用例执行成功 !')
                return status
            else:
                Log.error('双端状态与期望状态不一致，用例执行失败 !')
                return 0
        Log.error('请求返回有误！{}'.format(res))
        return 0

    def gwas_check(self, res):
        code = '00000'
        # taskId = res['data']
        # Log.debug('taskId is {}'.format(taskId))
        # [data_n, data_o] = self.get_data(taskId)
        # Log.info('本端数据为： {}'.format(data_n))
        # Log.info('对端数据为： {}'.format(data_o))
        if res['code'] == code:
            taskId = res['data']
            Log.debug('taskId is {}'.format(taskId))
            [data_n, data_o] = self.get_data(taskId)
            Log.info('本端数据为： {}'.format(data_n))
            Log.info('对端数据为： {}'.format(data_o))
            if self.compare(data_n, data_o):
                Log.info('compare result is True ,success !')
                return 1
            else:
                Log.error('compare result is False ,fail !')
                return 0
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
        list1.append(data_n['logicType'])
        list2.append(data_o['logicType'])
        Log.info('compare data is 本端：{}'.format(list1))
        Log.info('compare data is 对端：{}'.format(list2))
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

    def get_data_history(self, taskId):
        '根据发起taskid查询两端数据库数据'
        # 本端查询sql
        sql_n = 'select * from t_task_history where id = %d' % taskId
        # 对端查询sql
        sql_o = 'select * from t_task_history where startTaskId = %d' % taskId
        return [self.con_n.select_dic_single(sql=sql_n),
                self.con_o.select_dic_single(sql=sql_o)]

    def get_max_file_id(self):
        sql_max = 'SELECT max(id) from t_file'
        return [self.con_n.select_single(sql_max) + 6666, self.con_n.select_single(sql_max) + 6667]

    def gene_file_id_list(self, files, cookies):
        """"请求参数上传文件列表，返回文件id"""
        file_id = []
        if len(files) == 0:
            raise AssertionError('文件列表为空')
        for file in files:
            file_id.append(self.fh.upload_and_return_id(filename=file, para_id=self.upload_para_id,
                                                        fileType=self.fileType, cookies=cookies))

        return file_id


if __name__ == '__main__':
    Log.debug('*' * 50)
    cv = CalGwas(node=1)
    ck = Login(node=1)
    cookie = ck.get_cookie()
    # cookie =None
    para_id = 15
    data_id = 15001
    cv.base_gwas_start(para_id, data_id, cookie, isChange=0, maxFile=1)
    Log.debug('*' * 50)
