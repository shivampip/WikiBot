import os
import jsondiff
from rasa_nlu.model import Interpreter

class Bot:

    def trainNlu(self):
        os.system("python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose")

    def trainCore(self):
        os.system("python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue")

    def runCore(self):
        os.system("python -m rasa_core.run -d models/dialogue")

    def runBoth(self):
        os.system("python -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml")




class TestNlu:
    def __init__(self):
        self.interpreter= Interpreter.load("models/current/nlu")

    def runNlu(self, msg):
        return self.interpreter.parse(msg)


bot= Bot()
bot.trainNlu()
#bot.trainCore()
bot.runBoth()
exit()


mb= TestNlu()
mb.initNlu()
while(True):
    msg= input("You:- ")
    out= mb.runNlu(msg)
    out= json.dumps(out, indent=4)
    print("\n\n\n\nBot:- ",out)

