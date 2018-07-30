# import unittest
# import sys
# import time
#
# sys.path.append('../cases')
# from cases.test_quota_change import QuotaChangeDes
#
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTests(unittest.TestLoader().loadTestsFromTestCase(QuotaChangeDes))
#     now = time.strftime("%Y-%m-%d %H_%M_%S")
#     filename = '../report/' + now + '_result.html'
#     fp = open(filename, 'w')
#     runner = unittest.TextTestRunner(stream=fp, verbosity=2)
#     runner.run(suite)
#     fp.close()
from HTMLTestRunner import HTMLTestRunner
import unittest
import sys
import time
from dataHandle import DataHandle
from log import Log


sys.path.append('../cases')
sys.path.append('../common')

test_dir = '../cases'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

if __name__ == "__main__":
    Log.info('*'*100)
    Log.info('run START')

    now = time.strftime("%Y%m%d%H%M%S")
    filename = '../report/' + now + '_result.html'
    fp = open(filename, 'wb')

    # 新建result文件，并写入标题
    dh = DataHandle()
    title = [['id', 'name', 'actual', 'expect', 'result', str(now)]]
    dh.write_data(title)
    runner = HTMLTestRunner(stream=fp,
                            verbosity=2,
                            title='Test Report',
                            description='Implementation Example with: ')
    runner.run(discover)
    fp.close()
    Log.info('run FINISH')
    Log.info('*'*100)
