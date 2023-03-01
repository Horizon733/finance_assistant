import os
from pathlib import Path

this_path = Path(os.path.realpath(__file__))
DB_FILE = str(this_path.parent / "database.yml")

ELEMENTS = "elements"
ACCOUNT = "account"
EMAIL = "email"
CREDIT = "credit"

# db
DB_USER_COLUMN = "users"
DB_ACCOUNT_COLUMN = "account"
DB_HAS_CREDIT_CARD_COLUMN = "has_credit_card"
DB_CREDIT_CARD_COLUMN = "credit_card"
DB_TRANSACTIONS_COLUMN = "transactions"
DB_ACCOUNT_BALANCE_COLUMN = "account_balance"
DB_DESCRIPTION_COLUMN = "description"
DB_DATE_COLUMN = "date"
DB_AMOUNT_COLUMN = "amount"
DB_IMAGE_URL_COLUMN = "image_url"
DB_ELECTRICITY_BILL_COLUMN = "electricity_bill"
