""" creates the transaction functions"""
import random
from faker import Faker



def merchant_generator():
    """creates a fake merchant"""
    fake = Faker()

    mercchant_code = random.randrange(1, 99999)
    name = fake.company()
    description = "The all new Ford Taures, with enough seats to move your family from point A to Z while being the definition of style and comfort... It is a plug in hybrid..."

    merchant = {"code": mercchant_code, "name": name,
                "description": description}

    return merchant


def transaction_generator_deposit():
    """creates a test deposit"""
    mercchant_code = random.randrange(5, 99999)
    description = "deposited"
    transaction_deposit = {"type": "DEPOSIT", "method": "ACH", "amount": 100000,
                           "merchantCode": mercchant_code, "merchantName": "test",  "description": description, "accountNumber": "0011011575" }

    return transaction_deposit




def transaction_generator_purchase():
    """creates a test transaction"""
    mercchant_code = random.randrange(1, 99999)
  
    description = "the all new Ford Taures... It is a plug in hybrid"

    

    transaction_deposit = {"type": "PAYMENT", "method": "DEBIT_CARD", "amount": 50,
                           "merchantCode": mercchant_code, "merchantName": "testpay",  "description": description, "accountNumber": "0011011575"}

    return transaction_deposit


