# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormAction

#
#
class ModemCheckingAction(Action):

    def name(self) -> Text:
        return "action_Modem_Checking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        inventory = "888888"
        results = requests.get("https://asksupplychain.herokuapp.com/inventory?query=444444444444").json()
        if results:
            inventory = results[0]["Inventory"]
            modemstatus = "Successful"

    #    # message = "Active response" + inventory + "rrrrr" 
    #     print ("My name is Mamun")
        dispatcher.utter_message("See the below uptime information: \n Modem Up-time: {} \n Modem Status: {}".format(inventory,modemstatus))
       
#https://asksupplychain.herokuapp.com/inventory?query=444444444444
        return []

class ModemRebootingAction(Action):

    def name(self) -> Text:
        return "action_Modem_Reboot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #inventory = "888888"
        results = requests.get("https://asksupplychain.herokuapp.com/inventory?query=444444444444").json()
        if results:
            inventory = results[0]["Inventory"]
           # modemstatus = "Successful"
            dispatcher.utter_message("Successfully connected to the modem. I'm rebooting your modem now, it should take about 2 minutes.")
        else:
            dispatcher.utter_message("Modem is not responding")

        return[]
       # return [SlotSet("inventory_value", inventory)]
