while True:
    try:
        num_of_tickets = int(input('Введите необходимое количество билетов целым числом больше нуля: \n'))
    except ValueError as err:
        print('Неверный ввод')
    else:
        if num_of_tickets < 0:
            print('Неверный ввод')
        else:
            break

cost = 0

if num_of_tickets != 0:
    print('Введите возраст участников')

for i in range(1, int(num_of_tickets) + 1):
    while True:
        try:
            age = int(input(f'Введите возраст {i}-го посетителя:\n'))
            if age < 18:
                cost += 0
            elif 18 <= age < 25:
                cost += 990
            elif age >= 25:
                cost += 1390
        except ValueError as err:
            print('Неверный ввод')
        else:
            if age < 0:
                print('Неверный ввод')
            elif age > 100:
                print('Неверный ввод, Вам не может быть столько лет')
            else:
                break

if num_of_tickets > 3:
    print(f'Ваша скидка составила: {cost*0.1}')
    print(f'Итого к оплате: {cost - cost*0.1}')
else:
    print(f'Итого к оплате: {cost}')


