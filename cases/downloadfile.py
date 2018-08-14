from common.Base import Base
from cases.login import Login
from common.log import Log
import requests
from common.sql import sql
from common.dataHandle import DataHandle
import random


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
        Log.info('download_task response data is {}，{}'.format(res.status_code, res.content))
        Log.debug('{}'.format(type(res)))
        Log.debug('{}'.format(type(res.content)))
        Log.info('{}'.format(res.content is not None))
        # 结果检查
        actual = self.download_check(res, flag)
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
        Log.info('download_public_task response data is {}，{}'.format(res.status_code, res.content))
        Log.debug('{}'.format(type(res)))
        Log.debug('{}'.format(type(res.content)))
        Log.info('{}'.format(res.content is not None))
        # 结果检查
        actual = self.download_check(res, flag)
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
        req_para['taskIdList'] = self.get_task_id(eval(req_para['taskIdList']))
        data_source[0][5] = req_para['taskIdList']
        Log.info('download_public_history request data is {}'.format(req_para))
        # 请求
        res = requests.post(url=url_download_task, headers=Base.headers, cookies=cookies,
                            data=Base.sign(req_para))
        Log.info('download_public_history response data is {}，{}'.format(res.status_code, res.content))
        Log.debug('{}'.format(type(res)))
        Log.debug('{}'.format(type(res.content)))
        Log.info('{}'.format(res.content is not None))
        # 结果检查
        actual = self.download_check(res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def download_check(self, res, flag):
        code = 13333
        if not flag and eval(res.json()["code"]) == code:
            Log.info('请求返回错误:{}'.format(res.json()))
            return 0
        elif res.content is not None and res.status_code == 200:
            Log.info('文件下载接口ok')
            return 1

        return not flag

    def get_task_id(self, num):
        sql_taskid = 'select id from t_task order by id desc '
        res = self.base_get_task_id(sql_taskid, num)
        return res

    def get_history_task_id(self, num):
        sql_taskid = 'select id from t_task_history order by id desc '
        res = self.base_get_task_id(sql_taskid, num)
        return res

    def base_get_task_id(self, sql_taskid, num):
        """获取协同计算task id"""
        sql_taskid = sql_taskid
        id_list = list(self.con_n.select(sql_taskid))
        Log.debug(id_list)
        if len(id_list) < num:
            raise AssertionError('超长了')
        res = []
        for i in range(num):
            res.append(id_list[i][0])
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
