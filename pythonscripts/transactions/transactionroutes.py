"""sends the data to the transactin microservice"""
import requests
import json

from createtransaction import transaction_generator_deposit
from createtransaction import transaction_generator_purchase

URL = "http://127.0.0.1:8080/api/transactions"
URL_TRANSFER = "http://127.0.0.1:8080/api/transactions/transfer"


def create_deposit_transaction_api():
    """sends transaction data through the api"""
    data = transaction_generator_deposit()
    json_data = json.dumps(data)
    post_transaction = requests.post(
        url=URL, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VybmFtZWtldmluIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTIxNzc0MSwiZXhwIjoxNjUwNDI3MzQxfQ.klj3DbSxFWcuhjsr6xXL0diYyBwAoGxDb5-IEP4dy9w"}, data=json_data)

    print(post_transaction)
    return post_transaction


create_deposit_transaction_api()

def create_payment_transaction_api():
    """sends a payment through the api"""
    data = transaction_generator_purchase()
    json_data = json.dumps(data)
    post_transaction = requests.post(
        url=URL, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VybmFtZWtldmluIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTIxNzc0MSwiZXhwIjoxNjUwNDI3MzQxfQ.klj3DbSxFWcuhjsr6xXL0diYyBwAoGxDb5-IEP4dy9w"}, data=json_data)
    return post_transaction


def create_transfer_transaction_api():
    """sends a transfer request through the api"""
    data = {'fromAccountNumber': "0011012156",
            "toAccountNumber": "0011017000", "amount": 2000, "memo": "testtransfer"}
    json_data = json.dumps(data)
    post_transaction = requests.post(
        url=URL_TRANSFER, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VybmFtZWtldmluIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTIxNzc0MSwiZXhwIjoxNjUwNDI3MzQxfQ.klj3DbSxFWcuhjsr6xXL0diYyBwAoGxDb5-IEP4dy9w"}, data=json_data)
    return post_transaction


def create_withdrawal_transaction_api():
    """sends a withdrawal request through the api"""
    data = {"type": "WITHDRAWAL", "method": "ATM", "amount": 250,
                           "merchantCode": "NONE", "merchantName": "No merchant",  "description": "Test Withdrawal", "accountNumber": "0011012156"}
    json_data = json.dumps(data)
    post_transaction = requests.post(
        url=URL, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VybmFtZWtldmluIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTIxNzc0MSwiZXhwIjoxNjUwNDI3MzQxfQ.klj3DbSxFWcuhjsr6xXL0diYyBwAoGxDb5-IEP4dy9w"}, data=json_data)
    return post_transaction

def create_refund_transaction_api():
    """sends a refund request through the api"""
    data = {"type": "REFUND", "method": "APP", "amount": 100,
                           "merchantCode": "NONE", "merchantName": "No merchant",  "description": "Test Refund", "accountNumber": "0011012156"}
    json_data = json.dumps(data)
    post_transaction = requests.post(
        url=URL, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VybmFtZWtldmluIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTIxNzc0MSwiZXhwIjoxNjUwNDI3MzQxfQ.klj3DbSxFWcuhjsr6xXL0diYyBwAoGxDb5-IEP4dy9w"}, data=json_data)
    return post_transaction

