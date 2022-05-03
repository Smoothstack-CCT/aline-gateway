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
        url=URL_BANK, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKdXN0aW4uUm9kZ2VycyIsImF1dGhvcml0eSI6ImFkbWluaXN0cmF0b3IiLCJpYXQiOjE2NTEwODE5NzEsImV4cCI6MTY1MjI5MTU3MX0.qd-cSMyJ-KowmYdC20q0ionGvPwJy0GfbnqvkxjL3Cg"}, data=jason_bank)

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
        url=URL_BRANCH, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKdXN0aW4uUm9kZ2VycyIsImF1dGhvcml0eSI6ImFkbWluaXN0cmF0b3IiLCJpYXQiOjE2NTEwODE5NzEsImV4cCI6MTY1MjI5MTU3MX0.qd-cSMyJ-KowmYdC20q0ionGvPwJy0GfbnqvkxjL3Cg"}, data=branch_json)
    return post_branch
