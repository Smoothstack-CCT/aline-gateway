""" creates user information to populate the database """

import random
from faker import Faker

import sys
sys.path.insert(
    0, '/Users/kevinlyons/Documents/code/capstone/aline-gateway-KDL/pythonscripts/applicationsandapplicants')
from applicantsandapplicationsroutes import application_generator_checking_and_savings_api

def create_user_data_admin():
    """ profile creator function """
    fake = Faker()

    three_digit = random.randrange(100, 999)
    four_digit = random.randrange(1000, 9999)

    first_name = fake.first_name()
    last_name = fake.last_name()

    full_name = first_name+"."+last_name
    email = full_name + "@gmail.com"

    password = "P@ssword1!"
    phone = "{}-{}-{}".format(three_digit, three_digit, four_digit)

    admin = {"role": "admin", "firstName": first_name, "lastName": last_name, "username": full_name,
             "email": email, "password": password, "phone": phone, "enabled": 1}

    return admin


def create_user_data_member():
    data = application_generator_checking_and_savings_api()
    data = data.json()
    print(data)
    created_members = data.get('createdMembers')
    membership_id = created_members[0]
    name = membership_id.get('name')
    membership_id = membership_id.get('membershipId')
    social_security = data.get('applicants')
    social_security = social_security[0]
    social_security = social_security.get('socialSecurity').split('-')

    username = str(name.replace(' ', '.'))

    last_four_ssn = social_security[2]

    new_member = {"role": "member", "username": username, "password": "P@ssword1!",
                  "membershipId": membership_id, "lastFourOfSSN": last_four_ssn}

    return new_member


create_user_data_member()