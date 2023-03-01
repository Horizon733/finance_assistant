from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, Restarted, ActiveLoop

from actions.utils import to_carousels
from database_utils.constants import EMAIL, CREDIT
from database_utils.database_utils import get_mini_statement, get_balance, is_valid_user


class ActionShowCreditMiniStatement(Action):

    def name(self) -> Text:
        return "action_show_credit_card_statement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        email = tracker.get_slot(EMAIL)
        if email is None:
            dispatcher.utter_message("Please login to check statement")
            return [ActiveLoop("login")]
        else:
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
        if email is None:
            dispatcher.utter_message("Please login to check statement")
            return [ActiveLoop("login")]
        else:
            is_value, balance = get_balance(email)
            print(balance)
            if is_value:
                dispatcher.utter_message(f"Your account balance is ${balance}")
            else:
                dispatcher.utter_message("Sorry, i was not able to find your account with us.")
        return []


class ActionSlotReset(Action):
    def name(self) -> Text:
        return "action_slot_reset"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        return [AllSlotsReset(), Restarted()]


class ActionLogin(Action):
    def name(self) -> Text:
        return "action_login"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        email = tracker.get_slot(EMAIL)
        is_valid = is_valid_user(email)
        if is_valid:
            dispatcher.utter_message(response="utter_login_success")
        else:
            dispatcher.utter_message(response="utter_login_failed")
            return [AllSlotsReset(), Restarted()]
        return []