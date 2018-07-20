from dataHandle import DataHandle
from loadConfig import LoadConfig
import unittest
from log import Log


class MMM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Log.info('MMM test start')
        cls.lc = LoadConfig()
        cls.domain = cls.lc.get_domain_h()
        cls.dh = DataHandle()

    def setUp(self):
        Log.debug('========')
        pass

    def test_common_method(self):
        """test framework"""
        url = self.lc.get_domain_h() + self.dh.get_path(43)
        Log.info('request url is %s' % url)
        para_source = self.dh.get_para(43)
        data_source = self.dh.get_data(140)
        for i in range(len(data_source)):
            req_para = DataHandle.combine_data(para_source, data_source[i])
            Log.info(req_para)
            actual = 0
            DataHandle.set_data(data_source[i], actual)
        self.dh.write_data(data_source)
        self.assertTrue(self.dh.check_result(data_source), msg="failed ,refer to result.csv")

    def tearDown(self):
        Log.debug('========')
        pass

    @classmethod
    def tearDownClass(cls):
        Log.info('MMM test end')
