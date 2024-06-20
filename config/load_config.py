import os
import configparser

basePath = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(basePath, 'config.ini')


class LoadConfig:

    def __init__(self):    
        self.__conf_parser = configparser.ConfigParser()
        self.__conf_parser.read(configPath, encoding='utf-8')
        self.url = "".join([self.get('URL', 'protocol'), "://", self.get('URL', 'host'), ":", self.get('URL', 'port')])
        
    def get(self, section, param):
        value = self.__conf_parser.get(section, param)
        return value

config=LoadConfig()