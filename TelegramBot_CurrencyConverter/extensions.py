
import requests
import json
from config import cur_dict

class APIExeption(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIExeption(f'Невозможно конвертировать одинаковые валюты "{base}". Введите команду заново.')

        try:
            quote_ticker = cur_dict[quote]
        except KeyError:
            raise APIExeption(f'Неподдерживаемая валюта "{quote}", повторите ввод команды')

        try:
            base_ticker = cur_dict[base]
        except KeyError:
            raise APIExeption(f'Неподдерживаемая валюта "{base}", повторите ввод команды')

        try:
            amount = float(amount)
        except ValueError:
            raise APIExeption(f'Неверное значение суммы валюты "{amount}", повторите ввод команды')

        req_cur_status = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(req_cur_status.content)[cur_dict[base]]
        # #    print(type(total_base))
        # text_outp = f'Стоимость {amount} {quote} в {base}ах равна {total_base * float(amount)}'
        # bot.send_message(message.chat.id, text_outp)
        return total_base

def get_info_bot(bot):
    dict_bot = bot.user.to_dict()
    with open('json_telebot.json', 'w', encoding='utf8') as my_json_file:
        json.dump(dict_bot, my_json_file, ensure_ascii=False, indent=4)

    with open('json_telebot.json', encoding='utf8') as my_json_file1:
        print(my_json_file1.read())
