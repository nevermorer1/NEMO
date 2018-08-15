from common.Base import Base
from cases.login import Login
from common.log import Log
import requests
from common.sql import sql
from common.dataHandle import DataHandle
import random
from json import JSONDecodeError


class DownloadFile(Base):
    lang = ['zh_CN', 'zh_HK', 'en_US']

    def __init__(self, node=1, path_id=1):
        self.node = node
        Base.__init__(self, node=self.node, path_id=path_id)
        self.node_o = 2 if self.node == 1 else 1
        # self.fh = FileHandle(node=self.node)
        # 本端数据库
        self.con_n = sql(node=self.node)

    def base_download_task(self, para_id, data_id, cookies, flag=True):
        """协同计算-批量下载Excel"""
        # 获取请求url
        url_download_task = self.domain + Base.dh.get_path(para_id)
        Log.info('download_task request url : {}'.format(url_download_task))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 查找task id
        req_para['taskIdList'] = self.get_task_id(eval(req_para['taskIdList']))
        data_source[0][5] = req_para['taskIdList']
        Log.info('download_task request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_download_task, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para))
        Log.info('download_task response data is {}'.format(res.status_code))
        # 结果检查
        actual = self.new_check(res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_download_public_task(self, para_id, data_id, cookies, flag=True):
        """协同计算详情下载excel"""
        # 获取请求url
        url_download_task = self.domain + Base.dh.get_path(para_id)
        Log.info('download_public_task request url : {}'.format(url_download_task))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 查找task id
        req_para['taskId'] = self.get_task_id(num=1)[0]
        data_source[0][5] = req_para['taskId']
        Log.info('download_public_task request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_download_task, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para))
        Log.info('download_public_task response data is {}'.format(res.status_code))
        # 结果检查
        actual = self.new_check(res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_download_public_history(self, para_id, data_id, cookies, flag=True):
        """历史记录—（批量）下载excel"""
        # 获取请求url
        url_download_task = self.domain + Base.dh.get_path(para_id)
        Log.info('download_public_history request url : {}'.format(url_download_task))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 查找task id
        req_para['taskIdList'] = self.get_history_task_id(eval(req_para['taskIdList']))
        data_source[0][5] = req_para['taskIdList']
        Log.info('download_public_history request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_download_task, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para))
        Log.info('download_public_history response data is {}'.format(res.status_code))
        # 结果检查
        actual = self.new_check(res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_download_history_task(self, para_id, data_id, cookies, flag=True):
        """历史记录—下载文件"""
        # 获取请求url
        url_download_task = self.domain + Base.dh.get_path(para_id)
        Log.info('download_history_task request url : {}'.format(url_download_task))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 查找task id
        req_para['taskId'] = self.get_history_task_id(num=1)[0]
        data_source[0][5] = req_para['taskId']
        Log.info('download_history_task request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_download_task, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para))
        Log.info('download_history_task response data is {}'.format(res.status_code))
        # 结果检查
        actual = self.new_check(res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_download_circuitry(self, para_id, data_id, cookies, flag=True):
        """逻辑管理-下载电路文件"""
        # 获取请求url
        url_download_task = self.domain + Base.dh.get_path(para_id)
        Log.info('download_circuitry request url : {}'.format(url_download_task))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 查找task id
        req_para['logicId'] = self.get_logic_id()[0]
        data_source[0][5] = req_para['logicId']
        Log.info('download_circuitry request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_download_task, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para))
        Log.info('download_circuitry response data is {}'.format(res.status_code))
        # 结果检查
        actual = self.new_check(res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def base_download_log_file(self, para_id, data_id, cookies, flag=True):
        """日志部分-下载log文件"""
        # 获取请求url
        url_download_task = self.domain + Base.dh.get_path(para_id)
        Log.info('download_log_file request url : {}'.format(url_download_task))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 查找task id
        req_para['userId'] = self.get_user_id(req_para['userId'])
        data_source[0][5] = req_para['userId']
        Log.info('download_log_file request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_download_task, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para))
        Log.info('download_log_file response data is {}'.format(res.status_code))
        # 结果检查
        actual = self.new_check(res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    @staticmethod
    def new_check(res, flag):
        """response对象.json对象异常捕获判定文件下载是否成功"""
        try:
            json_res = res.json()
            if not flag:
                Log.error('请求返回有误：{}'.format(json_res))
                Log.info('test success')
                return flag
            else:
                Log.error('文件下载失败，请求异常{}'.format(json_res))
                return not flag
        except JSONDecodeError as je:
            Log.info('-content type-:{}'.format(type(res.content)))
            Log.debug('-contest:{}-'.format(res.content))
            Log.info('-contest is None :{}'.format(res.content is None))
            return flag
        except Exception as e:
            Log.error('未知异常:{}'.format(e))
            return not flag

    @staticmethod
    def download_check(res, flag):
        # code = 13333
        Log.debug('test1:res是否有.json:{}'.format(res.json()))
        if not flag:
            try:
                json_res = res.json()
                Log.error('请求返回有误：{}'.format(json_res))
                return 0
            except Exception:
                Log.error("返回错误")
                return 1

        # if not flag and eval(res.json()["code"]) == code:
        #     Log.info('请求返回错误:{}'.format(res.json()))
        #     return 0
        elif res.content is not None and res.status_code == 200:
            Log.info('文件下载接口ok')
            return 1

        return not flag

    def get_user_id(self, loginName):
        sql_id = 'select id from t_user where loginName = \'%s\'' % loginName
        Log.debug('用户id查询sql：{}'.format(sql_id))
        userId = self.con_n.select_single(sql_id)
        Log.debug('用户{}查询userId：{}'.format(loginName, userId))
        return userId

    def get_task_id(self, num):
        sql_taskid = 'select id from t_task'
        res = self.base_get_task_id(sql_taskid, num)
        return res

    def get_history_task_id(self, num):
        sql_taskid = 'select id from t_task_history where target is not NULL '
        res = self.base_get_task_id(sql_taskid, num)
        return res

    def get_logic_id(self):
        sql_logic = 'select id from t_logic'
        res = self.base_get_task_id(sql_logic, 1)
        return res

    def base_get_task_id(self, sql_taskid, num):
        """获取协同计算task id"""
        sql_taskid = sql_taskid
        id_list = list(self.con_n.select(sql_taskid))
        Log.debug(id_list)
        if len(id_list) < num:
            raise AssertionError('超长了')
        random_id_list = random.sample(id_list, num)
        res = []
        for i in range(num):
            res.append(random_id_list[i][0])
        Log.debug(res)
        return res


if __name__ == '__main__':
    df = DownloadFile()
    # print(df.get_task_id(3))
    ck = Login(node=1)
    cookie = ck.get_cookie()
    para_id = 38
    data_id = 38001
    print(df.base_download_task(para_id, data_id, cookies=None, flag=False))
