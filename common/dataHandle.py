import csv
import os
import time
import random


class DataHandle:
    """
    to be
    """

    def __init__(self, source):
        self.data_source = ''.join(['../data/', source])
        self.para_source = ''.join(['../config/', source])
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        self.new_file = ''.join(['../result/', os.path.splitext(source)[0],
                                 '_result_', now, '.csv'])

    def get_data(self, num=None):
        res = []
        source = self.data_source
        with open(source, 'r') as f:
            reader = csv.reader(f)
            tem = []
            for i in reader:
                tem.append(i)
            # 去掉标题
            temp = tem[1:]
            if num is None:
                res = temp
            else:
                for j in temp:
                    if eval(j[0]) == num:
                        res.append(j)
        return res

    def write_data(self, data_list):
        title = ['id', 'name', 'actual', 'expect', 'result']
        try:
            with open(self.new_file, 'w', newline='') as f:
                csv_writer = csv.writer(f, dialect='excel')
                csv_writer.writerow(title)
                csv_writer.writerows(data_list)
        except Exception as e:
            raise AssertionError('result dir not exists !%s' % e)


if __name__ == '__main__':
    s = 'data.csv'
    dh = DataHandle(s)
    data = dh.get_data()
    print(data)
    new_data = []
    actual = [33, 66, 99, 88, 77]
    for i in data:
        if eval(i[3]) in actual:
            i[4] = 'pass'
            i[2] = i[3]
        else:
            i[4] = 'fail'
            i[2] = random.randint(0, 100)
    dh.write_data(data)
