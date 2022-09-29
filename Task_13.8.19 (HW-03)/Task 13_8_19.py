num_of_tickets = int(input('Введите необходимое количество билетов:\n'))
cost = 0

print('Введите возраст участников')
for i in range(1, num_of_tickets + 1):
    age = int(input(f'Введите возраст {i}-го посетителя:\n'))
    if age < 18:
        cost += 0
    elif 18 <= age < 25:
        cost += 990
    elif age >= 25:
        cost += 1390

if num_of_tickets > 3:
    print(f'Ваша скидка составила: {cost*0.1}')
    print(f'Итого к оплате: {cost - cost*0.1}')
else:
    print(f'Итого к оплате: {cost}')

