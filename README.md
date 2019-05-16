#### WikiBot
Demo RASA Bot

### Files detail

#### Bot specific files

| File        | Description  |
|:----------- |:-------------| 
| nlu.md      | For intent classification and entity extraction | 
| stories.md  | For dialog flow management |   
| domain.yml  | defining everything |
| actions.py  | All custom actions  |
| nlu_config.yml | Processing Pipeline  |


#### General files

| File        | Description  |
|:----------- |:-------------| 
| endpoints.yml | Connecting bot with action server | 
| as.py  | Shortcut to run action server |   
| bot.py | Shortcut to train and run bot |
| models (folder) | auto generated on model training |
| rasa_core.log | auto generated log file for rasa_core |
| other files  | Github related files  |


### Training

#### Training NLU
```
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
```

#### Training Core
```
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue
```

### Running

#### Running Action Server
```
python -m rasa_core_sdk.endpoint --actions actions
```

#### Running Bot
```
python -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml
```



