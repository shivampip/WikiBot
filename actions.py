from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet 

import wikipedia 


class ActionWiki(Action):
    def name(self):
        return "action_wiki"

    def run(self, dispatcher, tracker, domain):
        word= tracker.get_slot("word")
        dispatcher.utter_message("Word is {}".format(word)) 
        return []



class ActionServerRestart(Action):
    def name(self):
        return "action_server_restart"

    def run(self, dispatcher, tracker, domain):
        server= tracker.get_slot("server_name")
        dispatcher.utter_message("Restarting {} server".format(server)) 
        return []