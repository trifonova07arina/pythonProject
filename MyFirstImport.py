import telebot
import random
import requests
from bs4 import BeautifulSoup


token = '5925878704:AAHEQrm9If_OnecgjCZOmxari3UeQB5yBlE'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome = 'Привет! Я умный бот! Умею сочинять стихи, здороваться, отправлять картинки с котиками, предлагать варианты игр, скидывать музыку и интересные факты (/start /poem /cat /music /fact /Sticker /recommendations /game)'
    bot.send_message(message.from_user.id, welcome)
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton('Факт')
    button2 = telebot.types.KeyboardButton('Стихотворение')
    button3 = telebot.types.KeyboardButton('Котики')
    button4 = telebot.types.KeyboardButton('Музыка')
    button5 = telebot.types.KeyboardButton('Стикер')
    button6 = telebot.types.KeyboardButton('Игра')
    keyboard.add(button1, button2, button3, button4, button5,button6)
    bot.send_message(message.chat.id, welcome, reply_markup=keyboard)
@bot.message_handler(commands=['recommendations'])
def send_recommendations(message):
    recommendation = 'Убедительная просьба не нажимать на несколько команд в течение небольшого времени, так как isbjorn_bot не может выполнять множество действий сразу!'
    bot.send_message(message.chat.id,recommendation)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = random.randint(1,4)
    cat_img = open('cat_' + str(cat_number) + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)
@bot.message_handler(commands=['Sticker'])
def send_sticker(message):
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEHDc1jrXdQ8Xq2r09lH1n0G5TFuBCAWQAC-isAAqH_cEnTz87GDLnObiwE')

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворенье..."
    bot.send_message(message.chat.id, poem_text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_url = telebot.types.InlineKeyboardButton('Перейти', url='http://stihi.ru/')
    keyboard.add(button_url)
    bot.send_message(message.chat.id,'Больше стихотворений по ссылке ниже',reply_markup=keyboard)


@bot.message_handler(commands=['game'])
def send_game(message):
    resp = requests.get('https://stopgame.ru/games/catalog').content
    html_ = BeautifulSoup(resp, 'html.parser')
    game = random.choice(html_.find_all(class_='_card_67304_1'))
    game_name = game.attrs['href'][6:].replace('_', ' ')
    game_link = 'https://stopgame.ru/'+game.attrs['href']
    bot.send_message(message.chat.id, game_name)
    bot.send_message(message.chat.id, game_link)


@bot.message_handler(commands=['music'])
def send_music(message):
    song=open('John_Doan_-_The_Lamentation_of_Turlough_Ocarolan_60312889.mp3','rb')
    bot.send_audio(message.chat.id, song)


@bot.message_handler(commands=['fact'])
def send_fact(message):
    response = requests.get('https://i-fakt.ru/').content
    html = BeautifulSoup(response, 'html.parser')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs['href']
    bot.send_message(message.chat.id, fact_link)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == 'привет':
        bot.send_message(message.from_user.id, 'Дароф!!!!')
    elif message.text == 'Факт':
        send_fact(message)
    elif message.text == 'Котики':
        send_cat(message)
    elif message.text == 'Музыка':
        send_music(message)
    elif message.text == 'Стихотворение':
        send_poem(message)
    elif message.text == 'Стикер':
        send_sticker(message)
    elif message.text == 'Игра':
        send_game(message)

bot.polling()