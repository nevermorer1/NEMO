from dataHandle import DataHandle
from loadConfig import LoadConfig
import time
# import requests
import hashlib


# from log import Log


class Base:
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}
    lc = LoadConfig()
    dh = DataHandle()

    @staticmethod
    def make_password(password):
        return hashlib.md5(password.encode('utf-8')).hexdigest()

    @staticmethod
    def gene_username():
        return 'test{}'.format(int(time.strftime("%Y%m%d%H%M%S")))


if __name__ == "__main__":
    print(Base.gene_username())
