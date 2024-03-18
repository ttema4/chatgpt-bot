import telebot
import openai
from config import TOKEN, APIKEY

bot = telebot.TeleBot(TOKEN)
openai.api_key = APIKEY


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")


@bot.message_handler(content_types=['text'])
def start_message(message):
    response = openai.Completion.create(model="davinci-002",
                                        prompt=message.text,
                                        temperature=0.7,
                                        max_tokens=500)
    print(response)
    bot.send_message(message.chat.id,
                     response['choices'][0]['text'] if response['choices'][0]['text'] != '' else 'Не понял -____-')


bot.polling(non_stop=True)
