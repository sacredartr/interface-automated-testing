import yaml
import json
from common.logger import logger

class LoadData():

    def __init__(self):
        pass

    def load_yaml(self, file_path):
        logger.info("load {} yaml file......".format(file_path))
        with open(file_path, encoding='utf-8') as file:
            data = yaml.safe_load(file)
        return data

    def load_json(self, file_path):
        logger.info("load {} json file......".format(file_path))
        with open(file_path, encoding='utf-8') as file:
            data = json.load(file)
        return data