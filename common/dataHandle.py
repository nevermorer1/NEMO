import csv
import os
import time


class DataHandle:
    """
    测试数据读取、组合、结果写入

    """

    def __init__(self, source='data.csv', dirs='../config/'):
        self.data_source = ''.join(['../data/', source])
        self.para_source = ''.join([dirs, source])
        now = time.strftime("%Y%m%d%H%M%S")
        self.new_file = ''.join(['../result/', os.path.splitext(source)[0],
                                 '_result_', now, '.csv'])

    @staticmethod
    def get_list(source, num=None, ):
        """
        获取指定行数据
        :param source:
        :param num:
        :return: list
        """
        res = []
        with open(source, 'r') as f:
            reader = csv.reader(f)
            tem = []
            for i in reader:
                tem.append(i)
            # 去掉标题
            temp = tem[1:]
            # 特定行存入结果
            if num is None:
                res = temp
            else:
                for j in temp:
                    if eval(j[0]) == num:
                        res.append(j)
        return res

    def get_data(self, num=None):
        """
        返回列表组成的列表[[],[]]
        :param num:
        :return:
        """
        return self.get_list(source=self.data_source, num=num)

    @staticmethod
    def set_data(data_ori, act):
        """
        设置单条数据测试结果
        :param data_ori:
        :param act:
        :return:
        """
        try:
            data_ori[2] = act
            if act == eval(data_ori[3]):
                data_ori[4] = 'success'
            else:
                data_ori[4] = 'fail'
        except IndexError as e:
            print('error %s' % e)
        # return data_ori

    def write_data(self, data_list):
        """
        写入结果
        :param data_list:
        :return:
        """
        title = ['id', 'name', 'actual', 'expect', 'result']
        try:
            with open(self.new_file, 'w', newline='') as f:
                csv_writer = csv.writer(f, dialect='excel')
                csv_writer.writerow(title)
                csv_writer.writerows(data_list)
        except Exception as e:
            raise AssertionError('result dir not exists !%s' % e)

    @staticmethod
    def combine_data(para_source, data_source):
        """
        组合参数列表与数据列表
        :param para_source:[]
        :param data_source:[]
        :return:{}
        """
        p = para_source[3:]
        d = data_source[5:]
        co = len(p) - len(d)
        # if co < 0:
        #     raise AssertionError('data too long ,please check data !')
        for i in range(co):
            d.append('')

        res = dict(zip(p, d))
        # try:
        #     for i, j in zip(para_source[3:], data_source[5:]):
        #         res[i] = j
        # except IndexError as e:
        #     print('error %s' % e)
        #     raise AssertionError('combine_data error !')
        # return res
        return res

    @staticmethod
    def combine_req(para_source, data_source_list):
        res = []
        for data_source in data_source_list:
            res.append(DataHandle.combine_data(para_source=para_source,
                                               data_source=data_source))
        return res

    def get_req_para(self,data_id, para_id):

        pass

    @staticmethod
    def get_para(para_id=None):
        """
        读取csv文件中请求数据参数
        :param para_id:
        :return:
        """
        file = '../config/para.csv'
        res = DataHandle.get_list(num=para_id, source=file)[0]
        # 删除空str
        while '' in res:
            res.remove('')
        return res

    @staticmethod
    def get_path(para_id):
        """
        读取请求路径
        :param para_id:
        :return: '/user/login'
        """
        return DataHandle.get_para(para_id)[2]


if __name__ == '__main__':
    # data = dh.get_data()
    # print(data)
    # new_data = []
    # actual = [33, 66, 99, 88, 77]
    # for i in data:
    #     dh.set_data(i, 33)
    #
    # dh.write_data(data)
    para_source1 = DataHandle.get_para(3)
    print(para_source1)
    s = 'data.csv'
    dh = DataHandle(s)
    # print(dh.get_list(dh.data_source,9))
    data_source1 = dh.get_data(3)
    print(data_source1)

    print(DataHandle.combine_req(para_source=para_source1,
                                 data_source_list=data_source1))
