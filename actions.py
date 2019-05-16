from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet 

import wikipedia 


# There is a class for each custom action, This is for custom action 'action_wiki'
class ActionWiki(Action):

    # name method returns custom action name
    def name(self):
        return "action_wiki"

    # Here, we write logic, external api calls and else
    def run(self, dispatcher, tracker, domain):

        # Getting 'word' slot value
        word= tracker.get_slot("word")
        
        # Searching word on wikipedia and getting summary
        summary= wikipedia.summary(word) 

        # Sending response back to user
        dispatcher.utter_message(summary)

        return []



class ActionServerRestart(Action):
    def name(self):
        return "action_server_restart"

    def run(self, dispatcher, tracker, domain):

        # Getting server_name slot value
        server= tracker.get_slot("server_name")
        
        dispatcher.utter_message("Restarting {} server".format(server)) 

        # Logic to restart given server
        #
        #
        #

        # Acknoledgement
        dispatcher.utter_message("Server restarted successfully")
        #dispatcher.utter_message("Server couldn't be restarted")

        return []