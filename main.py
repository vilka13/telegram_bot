import telebot, wikipedia, re
from telebot import types
bot = telebot.TeleBot('5754103158:AAEuLy2CmsYej6U8-cBXvw_imqMptPh3gFE');

wikipedia.set_lang("ru")

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''

        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2

    except Exception as e:
        return 'There is no information about this in the encyclopedia'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, f'Hi, {m.from_user.first_name}!Давай начнем шифрование, дай мне файл и я его зашифрую! /help')

@bot.message_handler(commands=["help"])
def help(m, res=False):
     bot.send_message(m.chat.id, "Я бот который шифрует данные твои документы, но это не точно)")

@bot.message_handler(commands=["support"])
def support(m, res=False):
    bot.send_message(m.chat.id, "Если есть проблемы свяжись с моим создателем: @flmff")



@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(none_stop=True, interval=0)