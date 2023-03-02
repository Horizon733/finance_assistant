import yaml
from typing import Text

from .constants import DB_USER_COLUMN, DB_FILE, DB_TRANSACTIONS_COLUMN, ACCOUNT, DB_CREDIT_CARD_COLUMN, \
    DB_ACCOUNT_BALANCE_COLUMN, DB_ACCOUNT_COLUMN, DB_ELECTRICITY_BILL_COLUMN, DB_HAS_CREDIT_CARD_COLUMN

with open(DB_FILE, "r") as dbf:
    DATABASE = yaml.safe_load(dbf)


def is_valid_user(useremail: Text) -> bool:
    global DATABASE
    is_valid_user = False
    if useremail in DATABASE[DB_USER_COLUMN]:
        is_valid_user = True
    return is_valid_user


def get_mini_statement(email, type):
    global DATABASE
    is_valid = is_valid_user(email)
    if is_valid:
        if type == ACCOUNT:
            return True, DATABASE[DB_USER_COLUMN][email][DB_TRANSACTIONS_COLUMN]
        else:
            is_credit_card = DATABASE[DB_USER_COLUMN][email][DB_HAS_CREDIT_CARD_COLUMN]
            if is_credit_card:
                return True, DATABASE[DB_USER_COLUMN][email][DB_CREDIT_CARD_COLUMN][DB_TRANSACTIONS_COLUMN]
            else:
                return False, {"value": "No credit card associated with this account"}
    return False, {"value": "Sorry, i was not able to find your account with us."}


def get_balance(email):
    global DATABASE
    is_valid = is_valid_user(email)
    if is_valid:
        return True, DATABASE[DB_USER_COLUMN][email][DB_ACCOUNT_COLUMN][DB_ACCOUNT_BALANCE_COLUMN]
    else:
        return False, None


def get_electricity_bill_balance(email):
    global DATABASE
    is_valid = is_valid_user(email)
    if is_valid:
        return True, DATABASE[DB_USER_COLUMN][DB_ELECTRICITY_BILL_COLUMN].items()
    else:
        return False, None


def get_electricity_bill_balance(email):
    global DATABASE
    is_valid = is_valid_user(email)
    if is_valid:
        return True, DATABASE[DB_USER_COLUMN][DB_ELECTRICITY_BILL_COLUMN][DB_ACCOUNT_COLUMN]
    else:
        return False, None

