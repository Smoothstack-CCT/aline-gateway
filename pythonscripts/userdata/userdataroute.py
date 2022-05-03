import requests
import json
from userdata import create_user_data_admin
from userdata import create_user_data_member

URL = 'http://127.0.0.1:8080/api/'


def create_admin_api():

    data = create_user_data_admin()
    json_data = json.dumps(data)
    post_user = requests.post(
        url=f'{URL}users/registration', headers={'Content-Type': 'application/json'}, data=json_data)
    return post_user


def log_in():
    url = f'{URL}users/registration'
    data = create_admin_api()
    data = data.json()
    username = data['username']
    login_info = {'username': username, 'password': 'P@ssword1!'}
    json_login = json.dumps(login_info)

    get_login = requests.post(
        url=f'{URL}login', headers={'Content-Type': 'application/json'}, data=json_login)

    headers = get_login.headers
    bear_token = headers['Authorization']

    return bear_token


def create_member_api():
    data = create_user_data_member()
    json_data = json.dumps(data)
    post_user = requests.post(
        url=f'{URL}users/registration', headers={'Content-Type': 'application/json', 'Authorization': log_in()}, data=json_data)
    return post_user
