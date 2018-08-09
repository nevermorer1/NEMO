from common.Base import Base
from cases.login import Login
from common.log import Log
import requests
import random
from common.sql import sql
from common.dataHandle import DataHandle
from cases.filehandle import FileHandle


class ComputeVcf(Base):

    def __init__(self, node=1, path_id=1):
        self.node = node
        Base.__init__(self, node=self.node, path_id=path_id)
        self.node_o = 2 if self.node == 1 else 1
        # 文件上传接口para id
        self.upload_para_id = 10
        # vcf 文件类型 1
        self.fileType = 1

        self.fh = FileHandle(node=self.node)
        # 本端数据库
        self.con_n = sql(node=self.node)
        # 对端数据库
        self.con_o = sql(node=self.node_o)

    def base_compute_vcf(self, para_id, data_id, cookies,flag, calType=1, maxFile=0):
        """vcf协同计算  calType:1 随机查找vcf task ; 2 查找基因协同计算任务 3 GWAS 0 查找最大id+6666"""
        # 获取请求url
        url_compute_vcf = self.domain + Base.dh.get_path(para_id)
        Log.info('compute_vcf request url : {}'.format(url_compute_vcf))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 登录态判断
        if cookies is not None:
            # 不存在的fileid
            if maxFile:
                req_para['fileId'] = self.get_max_file_id()
            else:
                # file文件上传获取fileId
                req_para['fileId'] = self.gene_file_id(req_para['fileId'], cookies)

        # id不存在
        if not calType:
            req_para['taskId'] = self.get_max_task_id()
        else:
            req_para['taskId'] = self.get_task_id(calType)

        data_source[0][5] = req_para['taskId']
        data_source[0][6] = req_para['fileId']
        Log.info('compute_vcf request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_compute_vcf, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para)).json()
        Log.info('compute_vcf response data is {}'.format(res))
        # 结果检查
        actual = self.vcf_check(res,flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_compute_mul(self, para_id, data_id, cookies,flag, maxId=0, maxFile=0):
        """vcf  批量计算"""
        # 获取请求url
        url_compute_mul = self.domain + Base.dh.get_path(para_id)
        Log.info('compute_mul request url : {}'.format(url_compute_mul))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 登录态判断
        if cookies is not None:
            # 不存在的fileid
            if maxFile:
                req_para['fileId'] = self.get_max_file_id()
            else:
                # file文件上传获取fileId
                req_para['fileId'] = self.gene_file_id(req_para['fileId'], cookies)

        # taskId
        if maxId:
            req_para['taskId'] = self.get_vcf_max_task_id()
        else:
            req_para['taskId'] = self.get_vcf_task_id_list()

        data_source[0][5] = req_para['taskId']
        data_source[0][7] = req_para['fileId']
        Log.info('compute_vcf request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_compute_mul, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para)).json()
        Log.info('compute_vcf response data is {}'.format(res))
        # 结果检查
        actual = self.vcf_check(res,flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def vcf_check(self, res,flag):
        code = '00000'
        if flag and res['code'] != code:
            raise AssertionError('请求返回应该为成功，实际失败 {}'.format(res))
        if not flag and res['code'] == code:
            raise AssertionError('异常用例请求返回应该为失败，实际成功 {}'.format(res))
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
        max_id = self.con_n.select_single(sql_max)
        return [max_id + 6666, max_id + 6667]

    def get_vcf_max_task_id(self):
        """生成不存在vcf的taskId"""
        sql_max = 'SELECT max(id) from t_task where calType =1 and status =1'
        max_id = self.con_n.select_single(sql_max)
        return [max_id + 6666, max_id + 6667]

    def get_vcf_task_id_list(self):
        """生成vcf task id 列表"""
        sql_task_id = 'SELECT id from t_task where calType =1 and status =1'
        task_id = self.con_n.select(sql_task_id)
        if len(task_id)<2:
            raise AssertionError('vcf 协同计算任务数量少于2，{}'.format(task_id))
        return [task_id[-1][0], task_id[-2][0]]

    def get_max_file_id(self):
        """生成不存在的fileId"""
        sql_max = 'SELECT max(id) from t_file'
        return self.con_n.select_single(sql_max) + 6666

    def get_task_id(self, calType):
        """获取task id.返回随机id"""
        sql_task_id = 'SELECT id from t_task WHERE calType =%d and status =1' % calType
        res = self.con_n.select(sql_task_id)
        task_id = random.choice(res)[0]
        sql_temp = 'SELECT * from t_task WHERE id =%d' % task_id
        task_info = self.con_n.select_dic_single(sql_temp)
        Log.debug('task info is : {}'.format(task_info))
        return task_id

    def gene_file_id(self, file, cookies):
        """返回单个文件"""
        file_id = self.fh.upload_and_return_id(filename=file, para_id=self.upload_para_id,
                                               fileType=self.fileType, cookies=cookies)
        return file_id

    def gene_file_id_list(self, files, cookies):
        """"请求参数上传文件列表，返回文件id列表"""
        file_id = []
        if len(files) == 0:
            raise AssertionError('文件列表为空')
        for file in files:
            file_id.append(self.fh.upload_and_return_id(filename=file, para_id=self.upload_para_id,
                                                        fileType=self.fileType, cookies=cookies))

        return file_id


if __name__ == '__main__':
    Log.debug('*' * 50)
    cv = ComputeVcf(node=1)
    ck = Login(node=1)
    cookie = ck.get_cookie()
    para_id = 22
    data_id = 22001
    cv.base_compute_vcf(para_id, data_id, cookie)
    Log.debug('*' * 50)
