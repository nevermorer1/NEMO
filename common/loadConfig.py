import configparser
import os
import requests


class LoadConfig:
    def __init__(self):
        self.f = '\conf.conf'
        self.auth = self.get_auth()

    def get_auth(self):
        file_path = os.path.abspath('..\config') + self.f
        config = configparser.ConfigParser()
        try:
            config.read(file_path, encoding='utf-8')
        except Exception as e:
            raise AssertionError("read file err !" + str(e))
        return config['auth']['user'], config['auth']['passwd']

    def get_domain_all(self):
        # 获取域名
        file_path = os.path.abspath('..\config') + self.f
        config = configparser.ConfigParser()
        try:
            config.read(file_path, encoding='utf-8')
            # print(config.sections())
        except Exception as e:
            raise AssertionError("read file err !" + str(e))
            # print(e)
            # return "read file err !"
        # print(config.sections())
        # print(config.items('domain'))
        return [config['domain_h']['domain'],config['domain_b']['domain']]

    def get_domain_h(self):
        return self.get_domain_all()[0]

    def get_domain_b(self):
        return self.get_domain_all()[1]

    def get_cookie_data(self):
        # 后台用户登录，获取后续请求header，cookie
        # file = '\conf.conf'
        sec = 'login'
        domain = self.get_config_data()
        url = domain + '/admin/login'
        request_data = self.get_request_data(self.f, sec)
        res = requests.post(url=url, data=eval(request_data['data']),
                            auth=self.auth)
        if res.json()['status']['err_code'] != 0:
            raise AssertionError('login failed !')
        # print(res.cookies)
        return res.cookies

    @staticmethod
    def get_request_data(file, section):
        # 获取配置接口参数及请求格式
        # 返回字典res
        file_path = os.path.abspath('..\config') + file
        config = configparser.ConfigParser()
        try:
            config.read(file_path, encoding='utf-8')
            # print(config.sections())
        except Exception as e:
            raise AssertionError("read file err !" + str(e))
            # print(e)
            # return "read file err !"
        if config.has_section(section):
            method = config[section]['method']
            data = config[section]['data']
            # data = eval(config[section]['data'])  ##转换为字典
            res = {'method': method, 'data': data}
            return res
        else:
            raise AssertionError('section not exist !')
            # return 'section not exist !'

    @staticmethod
    def get_request_paras(file, section):
        # 获取配置接口参数
        # 返回字典res
        file_path = os.path.abspath('..\config') + file
        config = configparser.ConfigParser()
        try:
            config.read(file_path, encoding='utf-8')
            # print(config.sections())
        except Exception as e:
            # print(e)
            # return "read file err !"
            raise AssertionError("read file err !" + str(e))
        res = {}
        if config.has_section(section):
            for option in config.options(section):
                res[option] = config.get(section, option)
            return res
        else:
            raise AssertionError('section not exist !')


if __name__ == '__main__':
    #     print(os.path.abspath('..'))
    #     f = '\conf.conf'
    #     cfg = LoadConfig()
    #     cfg.get_cookie_data()
    #     print(cfg.get_config_data(f))
    #         print(f)
    #         s = 'login'
    #     cfg = LoadConfig()
    #     cfg.get_cookie_data()
    #     res = cfg.get_request_data(f, s)
    #     print(res)
    #     print(type(res))
    #     print(type(res['data']))
    cfg = LoadConfig()
    print(cfg.auth)
    print(cfg.get_config_data())
    # print(cfg.get_cookie_data())
    # for i in range(len(s)):
    #     # print(type(cfg.get_request_paras(f, s1)))
    #     print(cfg.get_request_paras(f, s[i]))


