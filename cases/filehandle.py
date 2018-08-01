from common.Base import Base
from cases.login import Login
from common.log import Log
import requests
import json
from common.sql import sql
import os
from common.dataHandle import DataHandle


class FileHandle(Base):

    def __init__(self, node=1, path_id=1):
        self.node = node
        self.s = sql(node=node)
        Base.__init__(self, node=node, path_id=path_id)
        # file 文件目录
        self.file_path = os.path.join(os.path.realpath(os.path.dirname(os.path.dirname(__file__))), 'data')
        Log.info('上传文件所在目录：{}'.format(self.file_path))

    def base_upload(self, para_id, data_id, cookies, isChange=0, noFile=0):
        """isChange:0 不变更文件名，1 变更文件名
            noFile:0 上传文件，1 无文件
        """
        # 获取请求url
        url_upload = self.domain + Base.dh.get_path(para_id)
        Log.info('upload request url : {}'.format(url_upload))
        # 获取请求数据
        data_source = self.dh.get_data(data_id)
        req_para = Base.get_req_para(para_id=para_id, data_id=data_id)
        # 是否含上传文件
        Log.debug('文件绝对路径：{}'.format(self.gene_file(req_para['fileName'])))
        Log.debug('********：{}'.format(type(self.gene_file(req_para['fileName']))))

        if not noFile:
            f = open(self.gene_file(req_para['fileName']), 'rb')
            Log.debug('*********{}****'.format(type(f)))
            files = {'file': f}
            Log.info('要上传的文件是 :{}'.format(f.name))
        else:
            files = {}
            Log.info('上传文件为空')
        # 是否更改文件名
        if isChange:
            req_para['fileName'] = self.change_name(req_para['fileName'])
            data_source[0][5] = req_para['fileName']
        # 接口数据类型转换
        req_para['fileType'] = eval(req_para['fileType'])
        req_para['fileSize'] = eval(req_para['fileSize'])
        Log.info('upload request data is {}'.format(json.dumps(req_para)))
        # 请求接口
        res = requests.post(url=url_upload, cookies=cookies,
                            data=req_para, files=files).json()
        Log.info('upload response data is {}'.format(res))
        # 结果检查
        actual = self.upload_check(res)
        # 结果写入
        DataHandle.set_data(data_source[0], actual)
        self.dh.write_data(data_source)
        # 结果检查
        return self.dh.check_result(data_source)

    def upload_and_return_id(self, filename, para_id, fileType, cookies):
        """ 上传文件，返回fileid"""
        # 获取请求url
        url_upload = self.domain + Base.dh.get_path(para_id)
        Log.info('upload request url : {}'.format(url_upload))
        # 获取请求数据格式
        req_para = Base.get_req_para(para_id=para_id, data_id=10001)
        # 拼接文件绝对路径
        req_para['fileName'] = filename
        Log.debug('文件绝对路径：{}'.format(self.gene_file(req_para['fileName'])))
        Log.debug('********：{}'.format(type(self.gene_file(req_para['fileName']))))

        try:
            f = open(self.gene_file(req_para['fileName']), 'rb')
            Log.debug('*********{}****'.format(type(f)))
            files = {'file': f}
            Log.info('要上传的文件是 :{}'.format(f.name))
        except Exception as e:
            Log.error('上传文件为空')
            raise AssertionError('文件不存在 ! {}'.format(e))

        # 接口数据设置
        req_para['fileType'] = fileType
        req_para['fileSize'] = 7000
        Log.info('upload request data is {}'.format(json.dumps(req_para)))
        # 请求接口
        try:
            res = requests.post(url=url_upload, cookies=cookies,
                                data=req_para, files=files).json()
            Log.info('upload response data is {}'.format(res))
        except Exception as e:
            raise AssertionError("文件上传失败！{}".format(e))

        return res['data']

    @staticmethod
    def change_name(name):
        """更改文件名"""
        return 'ch_' + name
        pass

    def gene_file(self, file_name):
        """文件绝对路径"""
        return os.path.join(self.file_path, file_name)

    @staticmethod
    def upload_check(res):
        """1 成功 0 失败"""
        code = '00000'
        message = '成功'
        if res["code"] == code and res['message'] == message \
                and isinstance(res['data'], int):
            Log.debug('actual res check is 1')
            return 1
        else:
            Log.debug('actual res check is 0')
            return 0
        pass


if __name__ == '__main__':
    fh = FileHandle(2, 1)
    # name = 'case_part1.txt'
    p_id = 10
    d_id = 10001
    cookies = Login(node=2, path_id=1).get_cookie()
    # cookies = None
    fh.base_upload(para_id=p_id, data_id=d_id, cookies=cookies, isChange=0, noFile=0)
    # print(fh.change_name(name))
    # print(fh.gene_file(name))
