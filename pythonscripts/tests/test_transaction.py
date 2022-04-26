import sys
sys.path.insert(
    0, '/Users/kevinlyons/Documents/code/capstone/aline-gateway-KDL/pythonscripts/transactions')
from transactionroutes import create_deposit_transaction_api
from transactionroutes import create_payment_transaction_api
from transactionroutes import create_transfer_transaction_api
from transactionroutes import create_withdrawal_transaction_api
from transactionroutes import create_refund_transaction_api

def test_create_deposit_transaction_api():
    resp = create_deposit_transaction_api()
    assert resp.status_code==200

def test_create_payment_transaction_api():
    resp = create_payment_transaction_api()
    assert resp.status_code==200

def test_create_transfer_transaction_api():
    resp = create_transfer_transaction_api()
    assert resp.status_code==200    

def test_create_withdrawal_transaction_api():
    resp = create_withdrawal_transaction_api()
    assert resp.status_code==200      

def test_create_refund_transaction_api():
    resp = create_refund_transaction_api()
    assert resp.status_code==200 