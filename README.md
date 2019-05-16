# WikiBot
Demo RASA Bot

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
