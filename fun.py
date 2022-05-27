
import requests
import random
from PIL import Image, ImageDraw


def getRandomLesson():
    import requests
    from random import randint
    import bs4
    array = []
    response = requests.get("https://zen.yandex.ru/id/5c014ebee79aa203d9ec6524")
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all('a', class_='card-image-compact-view__clickable')
    print(quotes)
    for quote in quotes:
        array.append(quote.get('href'))
    rnd = randint(0, len(array) - 1)
    return(array[rnd])


def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Приcлать случайный урок":
        bot.send_message(chat_id, text=getRandomLesson())



