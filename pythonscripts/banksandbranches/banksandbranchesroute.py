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
        url=URL_BANK, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VybmFtZWtldmluIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTEwMzQyOSwiZXhwIjoxNjUwMzEzMDI5fQ.Je7zHKIJSqns6nd_15TNZ4_iwMN4hbaM9-BAr5PXcCo"}, data=jason_bank)

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

    print(banks_info)
    print(branch_json)
    post_branch = requests.post(
        url=URL_BRANCH, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VybmFtZWtldmluIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTIxNzc0MSwiZXhwIjoxNjUwNDI3MzQxfQ.klj3DbSxFWcuhjsr6xXL0diYyBwAoGxDb5-IEP4dy9w"}, data=branch_json)
    return post_branch
