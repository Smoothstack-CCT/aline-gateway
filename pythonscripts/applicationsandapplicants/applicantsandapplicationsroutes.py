""" sends data to the underwriter"""
import requests
import json
import sys


sys.path.insert(
    0, '/Users/kevinlyons/Documents/code/capstone/aline-gateway-KDL/pythonscripts/applicationsandapplicants/')
from applicants import create_applicant_data


def applicant_generator_api():
    """ sends applicant data to underwriter"""
    URL_APPLICANT = "http://127.0.0.1:8080/api/applicants"
    applicant = create_applicant_data()

    applicant_json = json.dumps(applicant)

    post_applicant = requests.post(
        url=URL_APPLICANT, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKdXN0aW4uUm9kZ2VycyIsImF1dGhvcml0eSI6ImFkbWluaXN0cmF0b3IiLCJpYXQiOjE2NTEwODE5NzEsImV4cCI6MTY1MjI5MTU3MX0.qd-cSMyJ-KowmYdC20q0ionGvPwJy0GfbnqvkxjL3Cg"}, data=applicant_json)

    return post_applicant



def application_generator_checking_and_savings_api():
    """ creates new applicants and submits for applications"""
    # checking and savings
    URL_APPLICATION = "http://127.0.0.1:8080/api/applications"
    existing_user = applicant_generator_api()

    existing_user = existing_user.json()
    applicant_id = existing_user.get('id')

    application = {"applicationType": "CHECKING_AND_SAVINGS",
                   "noApplicants": True, "applicantIds": [applicant_id]}
    application = json.dumps(application)

    post_application = requests.post(
        url=URL_APPLICATION, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKdXN0aW4uUm9kZ2VycyIsImF1dGhvcml0eSI6ImFkbWluaXN0cmF0b3IiLCJpYXQiOjE2NTEwODE5NzEsImV4cCI6MTY1MjI5MTU3MX0.qd-cSMyJ-KowmYdC20q0ionGvPwJy0GfbnqvkxjL3Cg"}, data=application)

    return post_application



def application_generator_credit_card_api():
    """ creates new applicants and submits for applications"""
    # credit card
    URL_APPLICATION = "http://127.0.0.1:8080/api/applications"
    existing_user = applicant_generator_api()

    existing_user = existing_user.json()
    applicant_id = existing_user.get('id')

    application = {"applicationType": "CREDIT_CARD",
                   "noApplicants": True, "applicantIds": [applicant_id]}
    application = json.dumps(application)

    post_application = requests.post(
        url=URL_APPLICATION, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKdXN0aW4uUm9kZ2VycyIsImF1dGhvcml0eSI6ImFkbWluaXN0cmF0b3IiLCJpYXQiOjE2NTEwODE5NzEsImV4cCI6MTY1MjI5MTU3MX0.qd-cSMyJ-KowmYdC20q0ionGvPwJy0GfbnqvkxjL3Cg"}, data=application)

    return post_application

