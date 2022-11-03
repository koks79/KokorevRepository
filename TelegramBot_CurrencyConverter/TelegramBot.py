
import telebot
from extensions import APIExeption, CryptoConverter, get_info_bot
from config import cur_dict, TOKEN

bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды голосовые сообщения.
@bot.message_handler(content_types=['voice'])
def response_voice(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'https://youtu.be/poa_QBvtIBA')


@bot.message_handler(content_types=['photo'])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Неплохой мем, Ха-Ха..')


# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message: telebot.types.Message):
    pass


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    print(message.text)
    text = 'Я бот-конвертер валют. Для начала работы с ботом введите команду в виде: \n имя валюты, стоимость которой хотите узнать <пробел> \
имя валюты, в которой надо узнать цену первой валюты <пробел> \
количество переводимой (первой) валюты (если это количество - дробное число, используйте в качестве разделителя точку, не запятую!)\
\nЧтобы увидеть список всех доступных валют введите /values'
    bot.reply_to(message, f"Приветствую, \t{message.chat.username}. " + text)


@bot.message_handler(commands=['values'])
def availible_values(message: telebot.types.Message):
    text = 'Доступные к обмену валюты:'
    for cur in cur_dict.keys():
        text = '\n'.join([text, cur, ])
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def cur_convert(message: telebot.types.Message):
    try:
        values = message.text.lower().split(' ')

        if len(values) != 3:
            raise APIExeption('Не удалось обработать команду, неверное количество параметров. Введите команду заново.')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except APIExeption as err:
        bot.reply_to(message, f'Пользовательская ошибка\n{err}')
    except Exception as err:
        bot.reply_to(message, f'Невозможно обработать команду, ошибка\n{err},\nповторите ввод команды')
    else:
        text_outp = f'Стоимость {amount} {quote} в {base}ах равна {total_base*float(amount)}'
        bot.send_message(message.chat.id, text_outp)


bot.polling(none_stop=True)
get_info_bot(bot)

#----------------------------------------------------------------------------------------------------------------------

# dict_bot = bot.user.to_dict()
# with open('json_telebot.json', 'w', encoding='utf8') as my_json_file:
#     json.dump(dict_bot, my_json_file, ensure_ascii=False, indent=4)
#
# with open('json_telebot.json', encoding='utf8') as my_json_file1:
#     print(my_json_file1.read())


#----------------------------------------------------------------------------------------------------------------------
# r = requests.get(
#     'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')  # делаем запрос на сервер по переданному адресу
# print(r.content)
# print(r.status_code) # узнаем статус полученного ответа

# получение списка из json-ответа
# req = requests.get('https://baconipsum.com/api/?type=meat-and-filler') # попробуем поймать json ответ
# print(req.content)
# list_json = json.loads(req.content)
# print(type(list_json))
#
# for text in list_json:
#     print(text[:50], '\n')

# # получение словаря из json-ответа
# r1 = requests.get('https://api.github.com')
# print(type(r1.content))
# dict_json = json.loads(r1.content)
# print(type(dict_json))
# print(dict_json)
# print(dict_json['organization_url'])
# # запись-чтение в файл json
# with open('json_template.json', 'w', encoding='utf8') as my_json_file:
#     json.dump(dict_json, my_json_file, ensure_ascii=False, indent=4)
#
# with open('json_template.json', encoding='utf8') as my_json_file1:
#     print(my_json_file1.read())


# # POST запрос
# # как FORM
# r2 = requests.post('https://httpbin.org/post', data = {'key':'value'}) # отправляем пост запрос
# print(r2.content) # содержимое ответа и его обработка происходит так же, как и с гет-запросами, разницы никакой нет
#
# # как JSON
# data = {'key': 'value'}
# r3 = requests.post('https://httpbin.org/post', json=json.dumps(data))  # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON
# print(r3.content)
#
# r4 = requests.options('https://httpbin.org/get')
# print(r4.content)

# получение первого текста из генератора
# r5 = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# text_j = json.loads(r5.content)
# print(text_j[0])
