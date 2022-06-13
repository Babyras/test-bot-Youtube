from xml.dom.expatbuilder import ElementInfo
import telebot 
from telebot import types
import info
import db
import datetime
import downloader

print(f"Бот запущен!")
bot = telebot.TeleBot(info.bot_token)

@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Скачать МР3")
        btn_balance = types.InlineKeyboardButton("Баланс💰")          
        markup.add(btn1, btn_balance)
        bot.send_message(message.chat.id, text=f"Привет, {message.from_user.first_name}! ",reply_markup=markup)
        if (db.check_user_exists(message.chat.id) == False):
            db.create_user(message.chat.id,60)
    except:
        print("ERROR START")


 #   if     bot.send_message(message.chat.id, text=f"Привет,

@bot.message_handler(content_types='text')
def message_reply(message):
    try:
        print(f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')} {message.chat.id} - {message.text}")
        if (db.check_repeat_url(message.chat.id, message.text)):
            bot.send_message(message.chat.id, "Вы уже отправляли такую ссылку")
        elif(not db.check_repeat_url(message.chat.id, message.text)):
            if ('youtu' in message.text):
                db.add_url(message.chat.id, message.text)
                bot.send_message(message.chat.id, "Ваша ссылка добавлена в очередь")  
        elif (message.text == "Скачать МР3"):
            bot.send_message(message.chat.id, "Вставьте ссылку на видео")
        elif (message.text == "Баланс💰"):
            bot.send_message(message.chat.id, f"Ваш баланс {db.check_balance(message.chat.id)}💰")
        else:
            bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован ..")
    except:
        print("ERROR REPLY") 

bot.infinity_polling()

