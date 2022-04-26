import requests
import random
import json
from banksandbranches import branch_generator
from faker import Faker


def banks_generator_api():
    URL_BANK = "http://127.0.0.1:8080/api/banks"
    branch = branch_generator()
    bank = {"address": branch["address"], "city": branch["city"],
            "zipcode": branch["zipcode"], "state": branch["state"], "routingNumber": branch["routingNumber"]}

    jason_bank = json.dumps(bank)

    post_bank = requests.post(
        url=URL_BANK, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUZXN0dXNlcm5hbWUiLCJhdXRob3JpdHkiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNjUwOTM4MjIzLCJleHAiOjE2NTIxNDc4MjN9.mub5IO2Tx09dFP4w_ECAYjOiGWPw2eviKRPwLX6yOKI"}, data=jason_bank)

    return post_bank


def branch_generator_api():
    fake = Faker()
    URL_BRANCH = "http://127.0.0.1:8080/api/branches"
    banks_info = banks_generator_api().json()
    company_name = fake.company()
    three_digit = random.randrange(100, 999)
    four_digit = random.randrange(1000, 9999)

    bank_id = banks_info.get('id')

    del banks_info["routingNumber"]
    del banks_info["id"]

    banks_info["name"] = company_name
    banks_info["bankID"] = bank_id
    banks_info["phone"] = "{}-{}-{}".format(three_digit,
                                            three_digit, four_digit)

    branch_json = json.dumps(banks_info)

 
    post_branch = requests.post(
        url=URL_BRANCH, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUZXN0dXNlcm5hbWUiLCJhdXRob3JpdHkiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNjUwOTM4MjIzLCJleHAiOjE2NTIxNDc4MjN9.mub5IO2Tx09dFP4w_ECAYjOiGWPw2eviKRPwLX6yOKI"}, data=branch_json)
    return post_branch
