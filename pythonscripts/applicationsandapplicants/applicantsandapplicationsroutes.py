
import requests
import json
from applicants import create_applicant_data


def applicant_generator_api():
    URL_APPLICANT = "http://127.0.0.1:8080/api/applicants"
    applicant = create_applicant_data()

    applicant_json = json.dumps(applicant)

    post_applicant = requests.post(
        url=URL_APPLICANT, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VybmFtZWtldmluIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTEwMzQyOSwiZXhwIjoxNjUwMzEzMDI5fQ.Je7zHKIJSqns6nd_15TNZ4_iwMN4hbaM9-BAr5PXcCo"}, data=applicant_json)

    return post_applicant


def application_generator_checking_and_savings_api():
    URL_APPLICATION = "http://127.0.0.1:8080/api/applications"
    existing_user = applicant_generator_api()

    existing_user = existing_user.json()
    applicant_id = existing_user.get('id')

    application = {"applicationType": "CHECKING_AND_SAVINGS",
                   "noApplicants": True, "applicantIds": [applicant_id]}
    application = json.dumps(application)

    post_application = requests.post(
        url=URL_APPLICATION, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VybmFtZWtldmluIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTEwMzQyOSwiZXhwIjoxNjUwMzEzMDI5fQ.Je7zHKIJSqns6nd_15TNZ4_iwMN4hbaM9-BAr5PXcCo"}, data=application)

    return post_application


def application_generator_credit_card_api():
    URL_APPLICATION = "http://127.0.0.1:8080/api/applications"
    existing_user = applicant_generator_api()

    existing_user = existing_user.json()
    applicant_id = existing_user.get('id')

    application = {"applicationType": "CREDIT_CARD",
                   "noApplicants": True, "applicantIds": [applicant_id]}
    application = json.dumps(application)

    post_application = requests.post(
        url=URL_APPLICATION, headers={'Content-Type': 'application/json', "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VybmFtZWtldmluIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTEwMzQyOSwiZXhwIjoxNjUwMzEzMDI5fQ.Je7zHKIJSqns6nd_15TNZ4_iwMN4hbaM9-BAr5PXcCo"}, data=application)
   
    return post_application



