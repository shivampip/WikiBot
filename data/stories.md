
<!-- This is a story -->

## greeting
* greet
  - utter_greet


<!-- This is a story -->
## Wikipedia
* wiki{"word":"ram"}      <!-- When intent is 'wiki', get slot 'word' value -->
  - slot{"word":"ram"}    <!-- Set word = extracted value -->
  - utter_searching       <!-- Call utter searching (domaing.yml > template ) -->
  - action_wiki           <!-- Now call custom action 'action_wiki' -->

## Remider
  - action_alarm

  

## Restart Server
* restart_server{"server_name": "something"}
  - slot{"server_name": "something"}
  - action_server_restart





