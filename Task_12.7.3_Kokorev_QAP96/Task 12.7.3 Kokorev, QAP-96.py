per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposits_by_banks = per_cent.copy()
deposit = []
i = 0

money = int(input('Введите сумму денежных средств :\n'))

for key_percent in per_cent:
       deposit.append(round(money/100*per_cent.get(key_percent), 2))
       deposits_by_banks[key_percent] = deposit[i]
       i+=1

print(deposit) # требования задачи по выводу информации

print('Вы можете заработать в банках :\n')
for key, value in deposits_by_banks.items():
       print(key, value)

print('Максимальная сумма, которую вы можете заработать :', max(deposit))



