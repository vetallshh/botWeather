import telebot
import pyowm

bot = telebot.TeleBot('1058871016:AAEKczf1SNAfxaRXxJcJeTsKkCwdpFd4dwQ')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я погодный бот, в каком городе ты хочешь узнать погоду ?')

@bot.message_handler(content_types=['text'])
def send_text(message):
        place = message.text.lower() #input("В каком городе/стране ?: ")

        owm = pyowm.OWM('a6d13da2fb8d891c88c951c9c2d945ef', language='ru')
        observation = owm.weather_at_place(place)
        w = observation.get_weather()
        temp = w.get_temperature('celsius')['temp']

    
        bot.send_message(message.chat.id, 'В городе ' + place + ' сейчас ' + w.get_detailed_status() + ' Средняя температура сейчас: ' + str(temp) + " 👍")

bot.polling()






