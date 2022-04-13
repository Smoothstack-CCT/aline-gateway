import requests
import json
from userdata import create_user_data_admin
from userdata import create_user_data_member

URL = "http://127.0.0.1:8080/api/users/registration"

def create_admin_api():

    data = create_user_data_admin()
    json_data = json.dumps(data)
    post_user = requests.post(
    url=URL, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VybmFtZWtldmluIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTIxNzc0MSwiZXhwIjoxNjUwNDI3MzQxfQ.klj3DbSxFWcuhjsr6xXL0diYyBwAoGxDb5-IEP4dy9w"}, data=json_data)
    return post_user



def create_member_api():
    data = create_user_data_member()
    json_data = json.dumps(data)
    post_user = requests.post(
    url=URL, headers={'Content-Type': 'application/json', }, data=json_data)

    print(post_user)
    return post_user


create_member_api()