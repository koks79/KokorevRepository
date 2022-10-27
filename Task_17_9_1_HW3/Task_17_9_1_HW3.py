def sort_func(us_list):
    for i in range(len(us_list)):
        for j in range(len(us_list) - i - 1):
            if us_list[j] > us_list[j + 1]:
                us_list[j], us_list[j + 1] = user_list[j + 1], us_list[j]

    return us_list

def get_index_perebor(array, num):
    list_idx = []
    for i in range(0, len(array)-1):
        if (array[i] < num and array[i + 1] >= num) or array[i] == num or array[i] == array[i + 1]:
            list_idx.append(i)
    return list_idx

def get_index(array, element, left, right):
    #    len_arr = len(array)
    if left > right:
        return 0
    middle = (right + left) // 2
    if array[middle] < element and array[middle + 1] >= element:
        return middle
    # if array[middle] == array[middle+1]:
    #     array.pop(middle+1)
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return get_index(array, element, left, middle - 1)
    else:  # иначе в правой
        # if len_arr == len(array):
        #     if array[middle-1] == array[middle]:
        #         array.pop(middle)
        #         return get_index(array, element, middle + 1, right-1)
        return get_index(array, element, middle + 1, right)

user_list = []

while True:
    try:
        inp_num = input('Введите последовательность, "e" - для завершения ввода')
        if inp_num == 'e':
            break
        inp_num_fl = float(inp_num)
        user_list.append(inp_num_fl)
    except ValueError as err:
        print('Неверный ввод')

while True:
    try:
        user_num = float(input('Введите любое контрольное число: \n'))
    except ValueError as err:
        print('Неверный ввод')
    else:
        if user_num > max(user_list):
            print('Неверное контрольное число, большее макимального значения в списке')
        elif user_num < min(user_list):
            print('Неверное контрольное число, меньше минимального значения в списке')
        else:
            break

print("Введенная вами последовательность")
print(*user_list, sep='  ')
print(f'Введенное вами контрольное число\n{user_num}')
print('--------------------------\n')
print('Сортированный список')
sorted_user_list = sort_func(user_list)
print(sorted_user_list)
print('---------------------------\n')
s = get_index(sorted_user_list, user_num, 0, (len(user_list)-1))
print(
    f'Позиция элемента в сортированном списке(начиная с нулевого), который меньше введенного вами контрольного числа, а следующий за ним больше или равен этому числу\n')
print(s)
print(f'... и значение этого элемента равно  {sorted_user_list[s]}')

print(
    f'Список позиций элементов в сортированном списке(начиная с нулевого), которые меньше введенного вами контрольного числа, а следующий за ним больше или равен этому числу\n')
g = get_index_perebor(user_list, user_num)
print(g)
