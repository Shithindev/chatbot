
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import collections.abc
collections.Hashable=collections.abc.Hashable
import pyttsx3
import webbrowser
from chatterbot.logic import logic_adapter
from chatterbot.trainers import ListTrainer

bot=ChatBot('mybot',logic_adapters={'chatterbot.logic.MathematicalEvaluation',
                                    'chatterbot.logic.BestMatch'})
traine=ChatterBotCorpusTrainer(bot)
traine.train('chatterbot.corpus.english','chatterbot.corpus.english.conversations')
trainer=ListTrainer(bot)
trainer.train(['hello','hi,how can i help you today?',
               'hi','hi,how can i help you today?',
               'cancel order','which order do i need to cancel?',
               'Help me on cancelling order','which order do i need to cancel?',
               'ok','thannks for visiting us,have a wonderful day',
               'thanks,bye','you are welcome,bye'])

def speak(command):
    text_speech=pyttsx3.init()
    text_speech.say(command)
    text_speech.runAndWait()
while True:
    qns=input('Me:')
    if qns=='bye':
        print('bot:goodbye')
        speak('goodbye!')
        break
    elif 'search' in qns:
        print('searching.....',qns.split('search')[1])
        url='https://youtube.com/search?q='+qns.split('search')[1]
        print(url)
        try:
            webbrowser.get().open(url)
        except:
            print('check your internet connection')
    else:
        response=bot.get_response(qns)
        print('bot:',response)
        speak(response)

