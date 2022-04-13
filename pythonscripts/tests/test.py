

import sys
sys.path.insert(
    0, '/Users/kevinlyons/Documents/code/capstone/aline-gateway-KDL/pythonscripts/applicationsandapplicants')
from applicantsandapplicationsroutes import applicant_generator_api
from applicantsandapplicationsroutes import application_generator_credit_card_api
from applicantsandapplicationsroutes import application_generator_checking_and_savings_api


def test_applicant_api():
    resp = applicant_generator_api()
    assert resp.status_code==201

def test_application_credit_card_api():
    resp = application_generator_credit_card_api()
    assert resp.status_code==201


def test_application_checking_and_saving_api():
    resp = application_generator_checking_and_savings_api()
    assert resp.status_code==201

sys.path.insert(
    0, '/Users/kevinlyons/Documents/code/capstone/aline-gateway-KDL/pythonscripts/banksandbranches')
from banksandbranchesroute import banks_generator_api
from banksandbranchesroute import branch_generator_api


def test_banks_api():
    resp = banks_generator_api()
    assert resp.status_code==201

def test_branch_api():
    resp = branch_generator_api()
    assert resp.status_code==201


sys.path.insert(
    0, '/Users/kevinlyons/Documents/code/capstone/aline-gateway-KDL/pythonscripts/userdata')
from userdataroute import create_admin_api
from userdataroute import create_member_api

def test_userdata_admin_api():
    resp = create_admin_api()
    assert resp.status_code==201

def test_userdata_member_api():
    resp = create_member_api()
    assert resp.status_code==201


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
