"""creates bank address """
import random
from faker import Faker
fake = Faker()


def branch_generator():
    """bank generator function"""
    fake = Faker()
 # address generates and seperates

    routing_number = random.randrange(100000000, 999999999)
    street_name = fake.street_name()
    street_prefix = fake.building_number()
    city = fake.city()
    address = street_prefix + " " + street_name
    state = fake.state_abbr()
    fake_zip = fake.postcode()

    bank_address = {"address": address, "city": city,
                    "state": state, "zipcode": fake_zip, "routingNumber": routing_number}

    return bank_address
