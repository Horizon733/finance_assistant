from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.utils import to_carousels
from database_utils.constants import EMAIL, ACCOUNT, CREDIT
from database_utils.database_utils import get_mini_statement, get_balance, get_electricity_bill_balance


class ActionShowMiniStatement(Action):

    def name(self) -> Text:
        return "action_show_mini_statement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        email = tracker.get_slot(EMAIL)
        is_value, mini_statement = get_mini_statement(email, ACCOUNT)
        if is_value:
            carousel = to_carousels(mini_statement)
            dispatcher.utter_message(attachment=carousel)
        else:
            dispatcher.utter_message(mini_statement["value"])
        return []


class ActionShowCreditMiniStatement(Action):

    def name(self) -> Text:
        return "action_show_credit_mini_statement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        email = tracker.get_slot(EMAIL)
        is_value, mini_statement = get_mini_statement(email, CREDIT)
        if is_value:
            carousel = to_carousels(mini_statement)
            dispatcher.utter_message(attachment=carousel)
        else:
            dispatcher.utter_message(mini_statement["value"])
        return []


class ActionShowBalance(Action):

    def name(self) -> Text:
        return "action_show_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        email = tracker.get_slot(EMAIL)
        is_value, balance = get_balance(email)
        if is_value:
            dispatcher.utter_message(f"Your account balance is ${balance}")
        else:
            dispatcher.utter_message("Sorry, i was not able to find your account with us.")
        return []


class ActionAskBillPayConfirmAmount(Action):

    def name(self) -> Text:
        return "action_ask_bill_pay_confirm_amount"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        email = tracker.get_slot(EMAIL)
        is_value, balance = get_electricity_bill_balance(email)
        if is_value:
            dispatcher.utter_message(response="utter_confirm_amount".format(bill_amount=balance))
        else:
            dispatcher.utter_message("Sorry, i was not able to find your account with us.")
        return []

