from core.url_client import URLClient

class User(URLClient):

    def __init__(self, **kwargs):
        super(User, self).__init__( **kwargs)

    def login(self, data, json=None, **kwargs):
        return self.post("/openstack/skyline/api/v1/global/login", data, json, **kwargs)
    
    def switch_project(self, project_id=None, **kwargs):
        return self.post(f"/openstack/skyline/api/v1/global/switch_project/{project_id}", **kwargs)