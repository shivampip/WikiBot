## greeting
* greet
  - utter_greet
  

## Wikipedia
* wiki{"word":"ram"}
  - slot{"word":"ram"}
  - utter_searching
  - action_wiki


## Restart Server
* restart_server{"server_name": "something"}
  - slot{"server_name": "something"}
  - action_server_restart