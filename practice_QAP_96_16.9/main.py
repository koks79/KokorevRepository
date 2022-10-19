
from classes import Rectangle, Client

rect = Rectangle(25, 38, 45, 78)
print(rect.__str__())
print(f' Площадь прямоугольника равна {rect.get_area()}\n\n')

cl = Client('Иван', 'Петров', 'Москва', 50)
print(f'{cl}\n\n')

clients = [
    {
    'first_name': 'Иван',
    'second_name': 'Петров',
    'town': 'Рязань',
    'balance': 0
    },
    {
    'first_name': 'Петр',
    'second_name': 'Смирнов',
    'town': 'Вологда',
    'balance': 0
    },
    {
    'first_name': 'Николай',
    'second_name': 'Кузнецов',
    'town': 'Новосибирск',
    'balance': 0
    }
]
for client in clients:
    guest = Client(client.get('first_name'), client.get('second_name'), client.get('town'), client.get('balance'))
    print('-----------------------------')
    print(f'{guest.get_client_info()}')