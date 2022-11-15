# audio voice document
import telebot
from telebot import types #вызов для кнопки

bot = telebot.TeleBot('5648499780:AAHK2skhz2VG_1W5smuFE8YiMlTEN7hrb_8')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Hello, {message.from_user.full_name}!\nUse /help"
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['id'])
def id(message):
    mess = f"Hello, {message.from_user.id}!"
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['group'])
def tg_group(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Переход", url="https://t.me/shtraf_kg"))
    bot.send_message(message.chat.id, "Ссылка на группу", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton("/start")
    group = types.KeyboardButton("/group")
    id = types.KeyboardButton("/id")
    audio = types.KeyboardButton("/audio")
    voice = types.KeyboardButton("/voice")
    photo = types.KeyboardButton("/photo")
    document = types.KeyboardButton("/document")
    group_link = types.InlineKeyboardButton("Переход", url="https://t.me/shtraf_kg")
    markup.add(start, group, id, audio, voice, photo, document, group_link)
    bot.send_message(message.chat.id, "Кнопки снизу", reply_markup=markup)

@bot.message_handler(commands=['photo'])
def photo(message):
    photo = open("1.png", "rb")
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['audio'])
def audio(message):
    audio = open("mp3.mp3", "rb")
    bot.send_audio(message.chat.id, audio)

@bot.message_handler(commands=['voice'])
def voice(message):
    voice = open("ding.ogg", "rb")
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['document'])
def document(message):
    document = open("python.pdf", "rb")
    bot.send_document(message.chat.id, document)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, f"Hello, {message.from_user.full_name}!")
    elif message.text == 'Привет':
        bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}!")
    else:
        bot.send_message(message.chat.id, "Не понимаю тебя\nВведите /help")

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Зачем мне эта картинка? 😟")

@bot.message_handler(content_types=['sticker'])
def get_user_sticker(message):
    bot.send_message(message.chat.id, "Зачем мне этот стикер? 😟")



bot.polling(none_stop=True)