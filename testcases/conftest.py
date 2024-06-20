import os
import pytest
from common.load_data import LoadData


BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

load_data = LoadData()



def __get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = load_data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


def project_name2id(project_name, projects):
    project_id = ""
    for _item in projects:
        if project_name == projects[_item]["name"]:
            project_id = _item
            break
    return  project_id

def resolve_headers(response, token=False):
    headers = {'Content-Type': 'application/json'}
    if token:
        headers["X-Auth-Token"] = response.json()["keystone_token"]
    return headers


api_data = __get_data("api_test_data.yml")
