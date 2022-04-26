import inquirer
import sys

def continue_dialog():
    question = [
        inquirer.List('continue',
                message="Continue?",
                choices=["Yes","No"]),
    ]
    answer = inquirer.prompt(question)

    if answer['continue'] == "Yes":
        dialog_tree_start()
    
    else:
        return



def dialog_tree_start():
    question = [
    inquirer.List('option',
                  message="What would you like to create/do?",
                  choices=["Users", "Transactions", "Banks/Branches",
                           "Applications/Applicants", "exit"],

                  ), ]
    answer = inquirer.prompt(question)

   
    if answer['option'] == "Users":
        users_input()


    if answer['option'] == "Transactions":
       transaction_input()

    if answer['option'] == "Banks/Branches":
        banks_and_branches_input()

    if answer['option'] == "Applications/Applicants":
        appicants_and_applications_input()
    
    else: return

def users_input():
    sys.path.insert(
    0, '/Users/kevinlyons/Documents/code/capstone/aline-gateway-KDL/pythonscripts/userdata')
    from userdataroute import create_admin_api
    from userdataroute import create_member_api
    question = [
        inquirer.List('users',
                      message="What kind of user to create?",
                      choices=["Admin", "Member", "Back", "Exit"],

                      ), ]

    answer = inquirer.prompt(question)

    if answer['users'] == "Admin":
    
        create_admin_api()
        continue_dialog()

    if answer['users'] == "Member":
       create_member_api()
       continue_dialog()

    if answer['users'] == "Back":
        dialog_tree_start()
    
    else:
        return


def transaction_input():
    sys.path.insert(
    0, '/Users/kevinlyons/Documents/code/capstone/aline-gateway-KDL/pythonscripts/transactions')
    from transactionroutes import create_deposit_transaction_api
    from transactionroutes import create_payment_transaction_api
    from transactionroutes import create_transfer_transaction_api
    from transactionroutes import create_withdrawal_transaction_api
    from transactionroutes import create_refund_transaction_api
    question = [
        inquirer.List('transaction',
                      message="What kind of transaction would you like to do?",
                      choices=["Deposit", "Payment", "Transfer", "Withdrawl", "Refund", "Back", "Exit"],

                      ), ]

    answer = inquirer.prompt(question)

    if answer['transaction'] == "Deposit":
        create_deposit_transaction_api()
        continue_dialog()

    if answer['transaction'] == "Payment":
        create_payment_transaction_api()
        continue_dialog()
    
    if answer['transaction'] == "Transfer":
        create_transfer_transaction_api()
        continue_dialog()

    if answer['transaction'] == "Withdrawl":
        create_withdrawal_transaction_api()
        continue_dialog()
    
    if answer['transaction'] == "Refund":
        create_refund_transaction_api()
        continue_dialog()

    if answer['transaction'] == "Back":
        dialog_tree_start()
        continue_dialog()
    
    else:
        return


def banks_and_branches_input():
    sys.path.insert(
    0, '/Users/kevinlyons/Documents/code/capstone/aline-gateway-KDL/pythonscripts/banksandbranches')
    from banksandbranchesroute import banks_generator_api
    from banksandbranchesroute import branch_generator_api
    question = [
        inquirer.List('banks',
                      message="What kind of user to create?",
                      choices=["Banks", "Branches", "Back", "Exit"],

                      ), ]

    answer = inquirer.prompt(question)

    if answer['banks'] == "Banks":
    
        banks_generator_api()
        continue_dialog()

    if answer['banks'] == "Branches":
       branch_generator_api()
       continue_dialog()

    if answer['banks'] == "Back":
        dialog_tree_start()
        continue_dialog()
    
    else:
        return


def appicants_and_applications_input():
   sys.path.insert(0, '/Users/kevinlyons/Documents/code/capstone/aline-gateway-KDL/pythonscripts/applicationsandapplicants')
   from applicantsandapplicationsroutes import applicant_generator_api
   from applicantsandapplicationsroutes import application_generator_credit_card_api
   from applicantsandapplicationsroutes import application_generator_checking_and_savings_api

   question = [
        inquirer.List('applicants',
                      message="What kind of applicant/application?",
                      choices=["Applicant", "Application(Checking and Savings)","Application(Credit)", "Back", "Exit"],

                      ), ]

   answer = inquirer.prompt(question)

   if answer['applicants'] == "Applicant":
    
        applicant_generator_api()
        continue_dialog()

   if answer['applicants'] == "Application(Checking and Savings)":
       application_generator_checking_and_savings_api()
       continue_dialog()

   if answer['applicants'] == "Application(Credit)":
       application_generator_credit_card_api()
       continue_dialog()

   if answer['applicants'] == "Back":
        dialog_tree_start()
        continue_dialog()
    
   else:
        return