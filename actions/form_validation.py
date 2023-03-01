from typing import Text, List

from rasa.shared.core.constants import REQUESTED_SLOT
from rasa_sdk import FormValidationAction
from rasa_sdk.events import EventType

from database_utils.constants import EMAIL
from database_utils.database_utils import is_valid_user


class ValidateTransferForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_transfer_form"

    def validate_email(
            self,
            value: Text,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> List[EventType]:
        returned_slots = {}
        if value is not None and is_valid_user(value):
            returned_slots = {EMAIL: value}
        else:
            returned_slots = {REQUESTED_SLOT: EMAIL}
            if value is None:
                dispatcher.utter_message(template="utter_email_not_valid")
            elif not is_valid_user(value):
                dispatcher.utter_message(template="utter_email_not_registered")
        return returned_slots
