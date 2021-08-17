# Importing chatterbot
from chatterbot import ChatBot

# Create object of ChatBot class with Logic Adapter
bot = ChatBot(
    'Chappie',  
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///database.sqlite3'
)

while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

    if input() == 'au revoir':
        break
