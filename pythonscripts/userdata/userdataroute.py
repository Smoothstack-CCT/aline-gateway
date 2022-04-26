import requests
import json
from userdata import create_user_data_admin
from userdata import create_user_data_member

URL = "http://127.0.0.1:8080/api/users/registration"


def create_admin_api():

    data = create_user_data_admin()
    json_data = json.dumps(data)
    post_user = requests.post(
        url=URL, headers={'Content-Type': 'application/json'}, data=json_data)
    return post_user


def create_member_api():
    data = create_user_data_member()
    json_data = json.dumps(data)
    post_user = requests.post(
        url=URL, headers={'Content-Type': 'application/json',"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUZXN0dXNlcm5hbWUiLCJhdXRob3JpdHkiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNjUwOTM4MjIzLCJleHAiOjE2NTIxNDc4MjN9.mub5IO2Tx09dFP4w_ECAYjOiGWPw2eviKRPwLX6yOKI" }, data=json_data)

    print(post_user)
    return post_user
