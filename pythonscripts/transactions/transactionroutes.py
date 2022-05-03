"""sends the data to the transactin microservice"""
import requests
import json

from createtransaction import transaction_generator_deposit
from createtransaction import transaction_generator_purchase

from userdata import userdataroute

URL = 'http://127.0.0.1:8080/api/'



def create_deposit_transaction_api():
    """sends transaction data through the api"""
    data = transaction_generator_deposit()
    json_data = json.dumps(data)
    post_transaction = requests.post(
        url=f'{URL}transactions', headers={'Content-Type': 'application/json', "Authorization": userdataroute.log_in()}, data=json_data)
    return post_transaction


def create_payment_transaction_api():
    """sends a payment through the api"""
    data = transaction_generator_purchase()
    json_data = json.dumps(data)
    post_transaction = requests.post(
        url=f'{URL}transactions', headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUZXN0dXNlcm5hbWUiLCJhdXRob3JpdHkiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNjUwOTM4MjIzLCJleHAiOjE2NTIxNDc4MjN9.mub5IO2Tx09dFP4w_ECAYjOiGWPw2eviKRPwLX6yOKI"}, data=json_data)
    return post_transaction



def create_transfer_transaction_api():
    """sends a transfer request through the api"""
    data = {'fromAccountNumber': "0011011575",
            "toAccountNumber": "0011014221", "amount": 2000, "memo": "testtransfer"}
    json_data = json.dumps(data)
    post_transaction = requests.post(
        url=f'{URL}transactions/transfer', headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUZXN0dXNlcm5hbWUiLCJhdXRob3JpdHkiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNjUwOTM4MjIzLCJleHAiOjE2NTIxNDc4MjN9.mub5IO2Tx09dFP4w_ECAYjOiGWPw2eviKRPwLX6yOKI"}, data=json_data)
    return post_transaction


def create_withdrawal_transaction_api():
    """sends a withdrawal request through the api"""
    data = {"type": "WITHDRAWAL", "method": "ATM", "amount": 250,
            "merchantCode": "NONE", "merchantName": "No merchant",  "description": "Test Withdrawal", "accountNumber": "0011011575"}
    json_data = json.dumps(data)
    post_transaction = requests.post(
        url=f'{URL}transactions', headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUZXN0dXNlcm5hbWUiLCJhdXRob3JpdHkiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNjUwOTM4MjIzLCJleHAiOjE2NTIxNDc4MjN9.mub5IO2Tx09dFP4w_ECAYjOiGWPw2eviKRPwLX6yOKI"}, data=json_data)
    return post_transaction


def create_refund_transaction_api():
    """sends a refund request through the api"""
    data = {"type": "REFUND", "method": "APP", "amount": 100,
            "merchantCode": "NONE", "merchantName": "No merchant",  "description": "Test Refund", "accountNumber": "0011011575"}
    json_data = json.dumps(data)
    post_transaction = requests.post(
        url=f'{URL}transactions', headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUZXN0dXNlcm5hbWUiLCJhdXRob3JpdHkiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNjUwOTM4MjIzLCJleHAiOjE2NTIxNDc4MjN9.mub5IO2Tx09dFP4w_ECAYjOiGWPw2eviKRPwLX6yOKI"}, data=json_data)
    return post_transaction

