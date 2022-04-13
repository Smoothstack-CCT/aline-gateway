
import random
from faker import Faker
from datetime import date



amount_generator = random.randrange(20, 250)


def merchant_generator():
    fake = Faker()

    mercchant_code = random.randrange(1, 99999)
    name = fake.company()
    description = "The all new Ford Taures, with enough seats to move your family from point A to Z while being the definition of style and comfort... It is a plug in hybrid..."
    registeredAt = date.today()

    merchant = {"code": mercchant_code, "name": name,
                "description": description, "registeredAt": registeredAt}

    return merchant


def transaction_generator_deposit():
    mercchant_code = random.randrange(5, 99999)
    description = "deposited"
    transaction_deposit = {"type": "DEPOSIT", "method": "ACH", "amount": 100000,
                           "merchantCode": mercchant_code, "merchantName": "test",  "description": description, "accountNumber": "0011012156" }

    return transaction_deposit




def transaction_generator_purchase():
    
    mercchant_code = random.randrange(1, 99999)
  
    description = "the all new Ford Taures... It is a plug in hybrid"

    

    transaction_deposit = {"type": "PAYMENT", "method": "DEBIT_CARD", "amount": 50,
                           "merchantCode": mercchant_code, "merchantName": "testpayment",  "description": description, "accountNumber": "0011012156"}

    return transaction_deposit


