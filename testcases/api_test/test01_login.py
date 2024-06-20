import pytest
import allure
from api.user import User
from testcases.conftest import *
from common.logger import logger

user = User()

@allure.step("setp01 ==>> user login")
def step_1(username):
    logger.info(f"step02 ==>> username: {username}")


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic("api test")
@allure.feature("user login module")
class TestUserLogin():

    @allure.story("testcase--user login")
    @allure.description("user login api test")
    # @allure.issue("test01", name="user_login")
    # @allure.testcase("test01", name="user_login")
    @allure.title("testdata: [{domain},{project},{username},{password},{except_result},{except_code}]")
    @pytest.mark.single
    @pytest.mark.parametrize("domain, project, username, password, except_result, except_code",api_data["user_login"])
    def test_login(self, domain, project, username, password, except_result, except_code):
        
        logger.info("*************** start ***************")
        data = {"domain": domain, "username": username, "password": password}
        res_login = user.login(data)
        step_1(username)
        logger.info(f"code ==>> except_result {except_code}, actual_result {res_login.status_code} ")
        assert res_login.status_code == except_code

        cookies = res_login.cookies
        headers = resolve_headers(res_login, token=True)
        project_id = project_name2id(project, res_login.json()["projects"])
        assert  project_id
        project_domain={"project_domain_id": res_login.json()["project"]["domain"]["id"]}

        res_switch_project = user.switch_project(project_id,cookies=cookies,params=project_domain,headers=headers)
        headers = resolve_headers(res_switch_project, token=True)

        logger.info("*************** end ***************")
