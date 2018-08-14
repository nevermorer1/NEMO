from common.Base import Base
from common.log import Log
import requests
from common.dataHandle import DataHandle
import random
from historytest import HistoryTest


class HistoryGWAS(HistoryTest):
    gwas_sql = ['select * from t_task_history where calType=3 and status=3 and logicType like \'%1%\'',
                'select * from t_task_history where calType=3 and status=3 and logicType like \'%2%\'',
                'select * from t_task_history where calType=3 and status=3 and logicType like \'%3%\'',
                'select * from t_task_history where calType=3 and status=3 and logicType like \'%4%\'']

    def __init__(self, node=1, path_id=1):
        self.node = node
        HistoryTest.__init__(self, node=self.node, path_id=path_id)

    def base_get_maf_cal_result(self, para_id, data_id, cookies, flag):
        """历史记录-查询maf计算结果公共方法"""
        # 获取请求url
        url_get_maf_cal_result = self.domain + Base.dh.get_path(para_id)
        Log.info('get_vcf_maf_result request url : {}'.format(url_get_maf_cal_result))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 查询数据库taskId，随机选择查询
        req_para['taskId'] = self.get_maf_done_task_id()
        data_source[0][5] = req_para['taskId']
        # 数据库查询taskId为空处理
        if req_para['taskId'] is None:
            actual = not flag
            Log.error('数据库查询taskId为空，该用例未执行，失败')
        else:
            Log.info('get_vcf_cal_result request data is {}'.format(req_para))
            # 请求
            res = requests.post(url=url_get_maf_cal_result, headers=Base.headers, cookies=cookies,
                                data=Base.sign(req_para)).json()
            Log.info('get_vcf_cal_result response data is {}'.format(res))
            # 结果检查
            actual = self.get_maf_result_check(req_para['taskId'], res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def get_maf_done_task_id(self):
        """获取计算完成的 maf task id.返回随机id"""
        sql_task_id = self.gwas_sql[0]
        res = self.con_n.select(sql_task_id)
        return random.choice(res)[0]

    def get_maf_result_check(self, taskId, res, flag):
        """1 成功 0 失败"""
        code = '00000'
        if flag and res['code'] != code:
            Log.error('请求返回应该为成功，实际失败 {}'.format(res))
            return 0
        if not flag and res['code'] == code:
            Log.error('异常用例请求返回应该为失败，实际成功 {}'.format(res))
            return 1
        if res["code"] != code:
            Log.error('返回错误：{}'.format(res))
            return 0
        sql_res = 'select count(*) from t_task_result where taskId = %d and logicType=1' % taskId
        data_database = self.con_n.select_single(sql_res)
        Log.debug('=={}=='.format(data_database))
        data_res = res['totalCount']
        Log.debug('**{}**'.format(data_res))
        if data_database == data_res:
            Log.info('data equal, compare success')
            return 1
        Log.error('data different, compare fail')
        return 0

    def base_get_gwasgen_cal_result(self, para_id, data_id, cookies, flag):
        """历史记录-查询GWAS-基因型计算结果公共方法"""
        # 获取请求url
        url_get_gwasgen_cal_result = self.domain + Base.dh.get_path(para_id)
        Log.info('get_gwasgen_maf_result request url : {}'.format(url_get_gwasgen_cal_result))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 查询数据库taskId，随机选择查询
        req_para['taskId'] = self.get_gwasgen_done_task_id()
        req_para['pageNo'] = eval(req_para['pageNo'])
        req_para['pageSize'] = eval(req_para['pageSize'])
        data_source[0][5] = req_para['taskId']
        # 数据库查询taskId为空处理
        if req_para['taskId'] is None:
            actual = not flag
            Log.error('数据库查询taskId为空，该用例未执行，失败')
        else:
            Log.info('get_gwasgen_cal_result request data is {}'.format(req_para))
            # 请求
            res = requests.post(url=url_get_gwasgen_cal_result, headers=Base.headers, cookies=cookies,
                                data=Base.sign(req_para)).json()
            Log.info('get_gwasgen_cal_result response data is {}'.format(res))
            # 结果检查
            actual = self.get_gwasgen_result_check(req_para['taskId'], res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def get_gwasgen_done_task_id(self):
        """获取计算完成的 gen task id.返回随机id"""
        sql_task_id = self.gwas_sql[1]
        res = self.con_n.select(sql_task_id)
        return random.choice(res)[0]

    def get_gwasgen_result_check(self, taskId, res, flag):
        """1 成功 0 失败"""
        code = '00000'
        if flag and res['code'] != code:
            Log.error('请求返回应该为成功，实际失败 {}'.format(res))
            return 0
        if not flag and res['code'] == code:
            Log.error('异常用例请求返回应该为失败，实际成功 {}'.format(res))
            return 1
        if res["code"] != code:
            Log.error('返回错误：{}'.format(res))
            return 0
        sql_res = 'select count(*) from t_task_result where taskId = %d and logicType=2' % taskId
        data_database = self.con_n.select_single(sql_res)
        Log.debug('=={}=='.format(data_database))
        data_res = res['totalCount']
        Log.debug('**{}**'.format(data_res))
        if data_database == data_res:
            Log.info('data equal, compare success')
            return 1
        Log.error('data different, compare fail')
        return 0

    def base_get_Dominant_cal_result(self, para_id, data_id, cookies, flag):
        """历史记录-查询GWAS-显性计算结果公共方法"""
        # 获取请求url
        url_get_Dominant_cal_result = self.domain + Base.dh.get_path(para_id)
        Log.info('get_Dominant_maf_result request url : {}'.format(url_get_Dominant_cal_result))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 查询数据库taskId，随机选择查询
        req_para['taskId'] = self.get_Dominant_done_task_id()
        req_para['pageNo'] = eval(req_para['pageNo'])
        req_para['pageSize'] = eval(req_para['pageSize'])
        data_source[0][5] = req_para['taskId']
        # 数据库查询taskId为空处理
        if req_para['taskId'] is None:
            actual = not flag
            Log.error('数据库查询taskId为空，该用例未执行，失败')
        else:
            Log.info('get_Dominant_cal_result request data is {}'.format(req_para))
            # 请求
            res = requests.post(url=url_get_Dominant_cal_result, headers=Base.headers, cookies=cookies,
                                data=Base.sign(req_para)).json()
            Log.info('get_Dominant_cal_result response data is {}'.format(res))
            # 结果检查
            actual = self.get_Dominant_result_check(req_para['taskId'], res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def get_Dominant_done_task_id(self):
        """获取计算完成的Dominant task id.返回随机id"""
        sql_task_id = self.gwas_sql[2]
        res = self.con_n.select(sql_task_id)
        return random.choice(res)[0]

    def get_Dominant_result_check(self, taskId, res, flag):
        """1 成功 0 失败"""
        code = '00000'
        if flag and res['code'] != code:
            Log.error('请求返回应该为成功，实际失败 {}'.format(res))
            return 0
        if not flag and res['code'] == code:
            Log.error('异常用例请求返回应该为失败，实际成功 {}'.format(res))
            return 1
        if res["code"] != code:
            Log.error('返回错误：{}'.format(res))
            return 0
        sql_res = 'select count(*) from t_task_result where taskId = %d and logicType=3' % taskId
        data_database = self.con_n.select_single(sql_res)
        Log.debug('=={}=='.format(data_database))
        data_res = res['totalCount']
        Log.debug('**{}**'.format(data_res))
        if data_database == data_res:
            Log.info('data equal, compare success')
            return 1
        Log.error('data different, compare fail')
        return 0

    def base_get_Recessive_cal_result(self, para_id, data_id, cookies, flag):
        """历史记录-查询GWAS-隐性计算结果公共方法"""
        # 获取请求url
        url_get_Recessive_cal_result = self.domain + Base.dh.get_path(para_id)
        Log.info('get_Recessive_maf_result request url : {}'.format(url_get_Recessive_cal_result))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 查询数据库taskId，随机选择查询
        req_para['taskId'] = self.get_Recessive_done_task_id()
        req_para['pageNo'] = eval(req_para['pageNo'])
        req_para['pageSize'] = eval(req_para['pageSize'])
        data_source[0][5] = req_para['taskId']
        # 数据库查询taskId为空处理
        if req_para['taskId'] is None:
            actual = not flag
            Log.error('数据库查询taskId为空，该用例未执行，失败')
        else:
            Log.info('get_Recessive_cal_result request data is {}'.format(req_para))
            # 请求
            res = requests.post(url=url_get_Recessive_cal_result, headers=Base.headers, cookies=cookies,
                                data=Base.sign(req_para)).json()
            Log.info('get_Recessive_cal_result response data is {}'.format(res))
            # 结果检查
            actual = self.get_Recessive_result_check(req_para['taskId'], res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def get_Recessive_done_task_id(self):
        """获取计算完成的 gen task id.返回随机id"""
        sql_task_id = self.gwas_sql[3]
        res = self.con_n.select(sql_task_id)
        return random.choice(res)[0]

    def get_Recessive_result_check(self, taskId, res, flag):
        """1 成功 0 失败"""
        code = '00000'
        if flag and res['code'] != code:
            Log.error('请求返回应该为成功，实际失败 {}'.format(res))
            return 0
        if not flag and res['code'] == code:
            Log.error('异常用例请求返回应该为失败，实际成功 {}'.format(res))
            return 1
        if res["code"] != code:
            Log.error('返回错误：{}'.format(res))
            return 0
        sql_res = 'select count(*) from t_task_result where taskId = %d and logicType=4' % taskId
        data_database = self.con_n.select_single(sql_res)
        Log.debug('=={}=='.format(data_database))
        data_res = res['totalCount']
        Log.debug('**{}**'.format(data_res))
        if data_database == data_res:
            Log.info('data equal, compare success')
            return 1
        Log.error('data different, compare fail')
        return 0

    def base_get_error_result(self, para_id, data_id, cookies, flag):
        """历史记录-查询GWAS-隐性计算结果公共方法"""
        # 获取请求url
        url_get_error_result = self.domain + Base.dh.get_path(para_id)
        Log.info('get_error_result request url : {}'.format(url_get_error_result))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 查询数据库taskId，随机选择查询
        req_para['taskId'] = self.get_Recessive_done_task_id()
        req_para['pageNo'] = eval(req_para['pageNo'])
        req_para['pageSize'] = eval(req_para['pageSize'])
        data_source[0][5] = req_para['taskId']
        # 数据库查询taskId为空处理
        if req_para['taskId'] is None:
            actual = not flag
            Log.error('数据库查询taskId为空，该用例未执行，失败')
        else:
            Log.info('get_error_result request data is {}'.format(req_para))
            # 请求
            res = requests.post(url=url_get_error_result, headers=Base.headers, cookies=cookies,
                                data=Base.sign(req_para)).json()
            Log.info('get_error_result response data is {}'.format(res))
            # 结果检查
            actual = self.get_error_result_check(req_para['taskId'], res, flag)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def get_error_task_id(self):
        """获取计算完成的 gen task id.返回随机id"""
        sql_task_id = self.gwas_sql[3]
        res = self.con_n.select(sql_task_id)
        return random.choice(res)[0]

    def get_error_check(self, taskId, res, flag):
        """1 成功 0 失败"""
        code = '00000'
        if flag and res['code'] != code:
            Log.error('请求返回应该为成功，实际失败 {}'.format(res))
            return 0
        if not flag and res['code'] == code:
            Log.error('异常用例请求返回应该为失败，实际成功 {}'.format(res))
            return 1
        if res["code"] != code:
            Log.error('返回错误：{}'.format(res))
            return 0
        sql_res = 'select count(*) from t_task_result where taskId = %d and logicType=4' % taskId
        data_database = self.con_n.select_single(sql_res)
        Log.debug('=={}=='.format(data_database))
        data_res = res['totalCount']
        Log.debug('**{}**'.format(data_res))
        if data_database == data_res:
            Log.info('data equal, compare success')
            return 1
        Log.error('data different, compare fail')
        return 0
