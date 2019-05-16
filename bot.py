import sys, getopt
import os
import json
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






def nice_print(msg):
    print("#"*40)
    print("### {}".format(msg))
    print("#"*40)


if __name__=='__main__':
    argv= sys.argv
    debug= False  
    train= False 
    run= False 

    if(len(argv)<=1):
        train= True 
        run= True 
    else:
        for arg in argv[1:]:
            if(arg=='debug'):
                debug= True     
                nice_print("DEGUGGING IS ON") 
            elif(arg=='train'):
                train= True  
            elif(arg=='run'):
                run= True 


    if(debug):
        mb= TestNlu()
        while(True):
            print('-'*50)
            msg= input("You:- ")
            out= mb.runNlu(msg)
            out= json.dumps(out, indent=4)
            print("\nBot:- ",out)
        exit()

    bot= Bot()
    if(train):
        bot.trainNlu()
        nice_print("NLU Trained successfully")
        bot.trainCore()
        nice_print("Core Trained successfully")
    if(run):
        bot.runBoth()

    

