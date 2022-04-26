
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
