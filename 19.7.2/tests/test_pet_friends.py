from api.api import PetFriends
from settings import valid_email, valid_password, nonvalid_email
import os

pf = PetFriends()

# тесты к заданию 19.7.2

def test_get_api_key_for_nonvalid_user(email=nonvalid_email, password=valid_password):
    """ Проверяем что запрос api ключа c неверными регистрационными данными возвращает статус 403 и в результате не содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    try:
        assert status == 403
    except:
        raise Exception('Invalid registration information')
    else:
        print('Invalid email or password')
        if 'key' in result:
            raise Exception('Server error')


def test_get_all_pets_with_nonvalid_key(filter='availible'):
    """ Проверяем что запрос всех питомцев c неверным фильтром возвращает статус 500.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее, используя для этого ключ,
    запрашиваем список всех питомцев и проверяем ответ сервера.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    try:
        assert status == 500
    except:
        raise Exception('Ошибка учетных данных')
    else:
        print('Filter of pets is incorrect')


def test_add_new_pet_with_nonvalid_data(name='♠♣♂◘♦☻', animal_type='двортерьерsjflsrjfgrhesgkjhrekgjhfkghfkjghrksjghreuhgreughfjevjfkbkjsdfghbkjsrghrugskrgksrgkrgbkshjrgbksrjbgvksfjgksrhksrjhgksfjhgksfgksfjhgksfrgbksfrhgksrjghksrjgksrjhfgksrjghfskrjghskfjvhbkjsfbvkjsrhfgkrhfgkwrhfiehwfjqpeufrwfhjrwkhfkjsrhfkrwsjfhraghforeghfkraejshfgrkjegfireughfiuerghfiuerfikuerh',
                                     age='6768769%(^&(^&(*^*(*&^^(*&^(*&^&*^(*&%^*&^%*&^', pet_photo='images/xkP_2nvuspY.jpg'):
    """Проверяем что можно добавить питомца с некорректными данными(комбинации алфавитов и спецсимволов)"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, pet_photo, age, animal_type, pet_photo,)

    # Сверяем полученный ответ с ожидаемым результатом
    try:
        assert status == 400
    except:
        raise Exception('Wrong data, but response code is not 400')


def test_unsuccessful_delete_self_pet():
    """Проверяем возможность удаления питомца c несуществующим id"""

    # Получаем ключ auth_key и запрашиваем список всех питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pets = pf.get_list_of_pets(auth_key, "")

    # Берём случайный id питомца из списка и проверяем, что в списке моих питомцев нет этого случайного id, отправляем запрос на удаление
    pet_id = '2638264264264279642yreuidysids4343432422'
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Проверяем что статус ответа равен 404
    if pet_id not in pets:
        assert status == 404
    else:
        raise Exception('id already exist')


def test_add_new_pet_with_invalid_data(name='Tony', animal_type='cats',
                                     age='Для современного мира дальнейшее развитие различных форм деятельности не оставляет шанса для существующих финансовых и административных условий. Внезапно, акционеры крупнейших компаний будут в равной степени предоставлены сами себе. Господа, сложившаяся структура организации играет важную роль в формировании новых предложений. Таким образом, высокотехнологичная концепция общественного уклада позволяет оценить значение новых предложений. Принимая во внимание показатели успешности, реализация намеченных плановых заданий предоставляет широкие возможности для модели развития. Равным образом, понимание сути ресурсосберегающих технологий не даёт нам иного выбора, кроме определения первоочередных требований. Имеется спорная точка зрения, гласящая примерно следующее: сторонники тоталитаризма в науке призывают нас к новым свершениям, которые, в свою очередь, должны быть объявлены нарушающими общечеловеческие нормы этики и морали. Господа, высокое качество позиционных исследований обеспечивает актуальность новых предложений. А ещё стремящиеся вытеснить традиционное производство, нанотехнологии, которые представляют собой яркий пример континентально-европейского типа политической культуры, будут преданы социально-демократической анафеме. Высокий уровень вовлечения представителей целевой аудитории является четким доказательством простого факта: курс на социально-ориентированный национальный проект выявляет срочную потребность экономической целесообразности принимаемых решений. Как принято считать, предприниматели в сети интернет превращены в посмешище, хотя само их существование приносит несомненную пользу обществу. Наше дело не так однозначно, как может показаться: социально-экономическое развитие не даёт нам иного выбора, кроме определения системы массового участия. Для современного мира существующая теория представляет собой интересный эксперимент проверки прогресса профессионального сообщества! Каждый из нас понимает очевидную вещь: современная методология разработки является качественно новой ступенью анализа существующих паттернов поведения. Как уже неоднократно упомянуто, предприниматели в сети интернет, вне зависимости от их уровня, должны быть призваны к ответу.', pet_photo='images/xkP_2nvuspY.jpg'):
    """Проверяем что можно добавить питомца с некорректными данными (строка возраст из 700+ символов)"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, pet_photo, age, animal_type, pet_photo,)

    # Сверяем полученный ответ с ожидаемым результатом
    try:
        assert status == 400
    except:
        raise Exception('Wrong data, but code is not 400')


def test_add_new_pet_simple_with_valid_data(name='Оурэлл', animal_type='попугай', age='3'):
    """Проверяем что можно добавить питомца без фото с корректными данными"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_foto_pet_with_valid_data(pet_photo='images/xkP_2nvuspY.jpg'):
    """Проверяем возможносmь добавления фотографии питомца"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

# Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Если список не пустой, то далее проверяем, что фото у питомца нет и пробуем добавить к нему фото
    if len(my_pets['pets']) > 0:
        for i in range(len(my_pets['pets'])):
            if not(my_pets['pets'][i]['pet_photo']):
                status, result = pf.add_foto_of_pet(auth_key, my_pets['pets'][i]['id'], pet_photo)
                # Проверяем что статус ответа = 200 и наличие фото
                assert status == 200
                assert result['pet_photo'] != ''
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_add_foto_pet_with_existing_foto(pet_photo='images/xkP_2nvuspY.jpg'):
    """Проверяем возможносmь добавления фотографии питомца, у которого уже есть фото"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

# Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Если список не пустой, то далее проверяем, что фото питомца есть и пробуем добавить к нему другое фото
    if len(my_pets['pets']) > 0:
        for i in range(len(my_pets['pets'])):
            if my_pets['pets'][i]['pet_photo']:
                existing_foto = my_pets['pets'][i]['pet_photo']
                status, result = pf.add_foto_of_pet(auth_key, my_pets['pets'][i]['id'], pet_photo)
                # Проверяем что статус ответа = 200 и что новое фото отличается от старого
                assert status == 200
                assert result['pet_photo'] == existing_foto
    else:
        # если спиcок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_add_new_pet_twice_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/xkP_2nvuspY.jpg'):
    """Проверяем что можно добавить одного и того же питомца дважды с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # получаем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Добавляем одного и того же питомца несколько раз и проверяем равны ли их имена
    for i in range(0, 5):
        temp_name = my_pets["pets"][i]["name"]
        temp_id = my_pets["pets"][i]["id"]
        status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
        # Заново получаем список моих питомцев
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Сверяем полученный ответ и одинаковы ли имена
        assert status == 200
        assert temp_name == my_pets["pets"][i]["name"]
        # у каждой питомца одинаковые данные, но разный id
#        assert temp_id == my_pets["pets"][i]["id"]

def test_get_all_pets_without_api_key(filter='my_pets'):
    """ Проверяем что будет, если запросим всех питомцев без api_key.
    Доступное значение параметра filter - 'my_pets' либо '' """

# c54d17df4275d39686072c1075abe6f9cb883da2995032d44a3bdb14
    auth_key = {'key': 'c54d17df4275d39686072'}

    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 403
#    assert len(result['pets']) > 0


#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
# позитивные тесты из материалов курса (19.5-6)

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/xkP_2nvuspY.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/QUAoXiQMvo0.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets['pets']

def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")



