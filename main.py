import telebot
from telebot import types
from config import TOKEN

registration = []

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def welcome(message):
    menu = types.InlineKeyboardMarkup(row_width=3)
    b1 = types.InlineKeyboardButton("ФИО",callback_data="name")
    b2 = types.InlineKeyboardButton("Телефон",callback_data="number")
    b3 = types.InlineKeyboardButton("Возраст",callback_data="age")
    menu.add(b1,b2,b3)
    bot.send_message(message.chat.id,"<b>Добавьте пошагово данные для регистрации</b>",parse_mode='html',reply_markup=menu)

@bot.callback_query_handler(func=lambda call:True)

def callback(call):
    if call.data == 'name':
        bot.send_message(call.message.chat.id,"<b>Введите ФИО полностью</b>",parse_mode='html')
    elif call.data == 'number':
        bot.send_message(call.message.chat.id,"<b>Введите номер телефона</b>",parse_mode='html')
    elif call.data == 'age':
        bot.send_message(call.message.chat.id,"<b>Введите свой возраст</b>",parse_mode='html')

@bot.message_handler(func=lambda message:True)

def user_input(message):
    if message.text is not None:
        registration.append(message.text)
        bot.send_message(message.chat.id,"<b>Данные сохранены</b>",parse_mode='html')
        save()

def save():
    if len(registration)>=3:
       with open("registration.txt","w") as f:
           f.write(f"ФИО: {registration[0]}\t")
           f.write(f"Телефон: {registration[1]}\t")
           f.write(f"Возраст: {registration[2]}\t")
    else:
        print("Мало информации")



bot.polling(non_stop=True)


    
    