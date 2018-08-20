# -*- coding:utf-8 -*-
import logging
import sys


class Log:

    @classmethod
    def setlog(cls):
        cls.logger = logging.getLogger(__name__)
        cls.logger.setLevel(level=logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s][%(levelname)-5s]:%(message)s')
        # 文件输出
        cls.file_handler = logging.FileHandler(r"../report/test.log")
        cls.file_handler.setFormatter(formatter)
        cls.file_handler.setLevel(level=logging.DEBUG)
        cls.logger.addHandler(cls.file_handler)
        # 控制台输出
        cls.stream_handler = logging.StreamHandler(sys.stdout)
        cls.stream_handler.setFormatter(formatter)
        cls.stream_handler.setLevel(level=logging.DEBUG)
        cls.logger.addHandler(cls.stream_handler)

    @classmethod
    def removehandler(cls):
        cls.logger.removeHandler(cls.file_handler)
        cls.logger.removeHandler(cls.stream_handler)

    @classmethod
    def debug(cls, message):
        Log.setlog()
        cls.logger.debug(message)
        Log.removehandler()

    @classmethod
    def info(cls, message):
        Log.setlog()
        cls.logger.info(message)
        Log.removehandler()

    @classmethod
    def warn(cls, message):
        Log.setlog()
        cls.logger.warn(message)
        Log.removehandler()

    @classmethod
    def error(cls, message):
        Log.setlog()
        cls.logger.error(message)
        Log.removehandler()


if __name__ == '__main__':
    Log.debug('debug')
    Log.info('info')
    Log.warn('warn')
    Log.error('error')
