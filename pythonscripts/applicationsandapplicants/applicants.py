""" creates user information to populate the database """

from faker import Faker
import datetime
import random


def create_applicant_data():
    """ profile creator function """
    fake = Faker()

    random_gender = random.randrange(1, 3)

    if random_gender == 1:
        gender = "MALE"

    else:
        gender = "FEMALE"

    three_digit = random.randrange(100, 999)
    four_digit = random.randrange(1000, 9999)

    month = random.randrange(1, 13)
    day = random.randrange(1, 31)
    year = random.randrange(1920, 2005)

    first_name = fake.first_name()
    last_name = fake.last_name()
    

    full_name = first_name+"."+last_name
    email = full_name + "@gmail.com"
    dob = f"{year}-{month}-{day}"
    dob = datetime.datetime.strptime(dob, '%Y-%m-%d')
    dob = datetime.datetime.strftime(dob, "%Y-%m-%d")
    ssn = fake.ssn()

    drivers_license = random.randrange(1000000000, 9999999999999)

    # address generates and seperates
    street_name = fake.street_name()
    street_prefix = fake.building_number()
    city = fake.city()
    address = street_prefix + " " + street_name
    state = fake.state_abbr()
    fake_zip = fake.postcode()

    password = "P@ssword1!"
    phone = "{}-{}-{}".format(three_digit, three_digit, four_digit)
    income = random.randrange(10000000, 2147483648, 1000)

    profile = {"gender": gender, "firstName": first_name, "lastName": last_name, "username": full_name, "email": email, "driversLicense": drivers_license, "dateOfBirth": dob, "socialSecurity": ssn, "phone": phone, "income": income,
               "password": password, "address": address, "city": city, "state": state, "zipcode": fake_zip, "mailingAddress": address, "mailingCity": city, "mailingState": state, "mailingZipcode": fake_zip}

    return profile
