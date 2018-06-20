from dataHandle import DataHandle
from loadConfig import LoadConfig
import unittest


class MMM(unittest.TestCase):
    def setUp(self):
        self.lc = LoadConfig()
        self.domain = self.lc.get_domain()
        self.dh = DataHandle()
        pass

    def test_common_method(self):
        """test framework"""
        url = self.lc.get_domain() + self.dh.get_path(3)
        print('request url is %s' % url)
        para_source = self.dh.get_para(3)
        data_source = self.dh.get_data(3)
        for i in range(len(data_source)):
            req_para = DataHandle.combine_data(para_source, data_source[i])
            print(req_para)
            actual = 33
            DataHandle.set_data(data_source[i], actual)
        self.dh.write_data(data_source)
        self.assertTrue(self.dh.check_result(data_source), msg="failed ,refer to result.csv")