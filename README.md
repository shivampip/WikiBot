#### WikiBot
Demo RASA Bot

## Getting Started

### Installation

* Clone the repo
```
git clone https://github.com/shivampip/WikiBot.git
cd WikiBot
```

### Run

* Run Action Server
```
python as.py
```

* Open saperate terminal/cmd 
* Train and Run
```
python bot.py
```

* Train only
```
python bot.py train
```

* Run only
```
python bot.py run
```

* Debug (see internal working of NLU)
```
python bot.py debug
```


### Files detail

#### File exploration sequence

1.  nlu.md
2.  domain.yml
3.  stories.md
4.  actions.py
5.  nlu_config.yml

#### Bot specific files

| File        | Description  |
|:----------- |:-------------| 
| nlu.md      | For intent classification and entity extraction | 
| stories.md  | For dialog flow management |   
| domain.yml  | defining everything |
| actions.py  | All custom actions  |
| nlu_config.yml | Processing Pipeline  |


#### General files (Almost same for all projects)

| File        | Description  |
|:----------- |:-------------| 
| endpoints.yml | Connecting bot with action server | 
| as.py  | Shortcut to run action server |   
| bot.py | Shortcut to train and run bot |
| models (folder) | auto generated on model training |
| rasa_core.log | auto generated log file for rasa_core |
| other files  | Github related files  |






