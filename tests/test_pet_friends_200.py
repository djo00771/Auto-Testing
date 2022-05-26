from api import PetFriends
from settings import *
import os


pf = PetFriends()


def test_api_key_for_valid_user(email=valid_email, password=valid_password):
    """Тест на получение api key"""

    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result
    print(f'\nstatus_code is - {status}')
# --------------------------------------------------------------------------------------------------------


def test_get_all_pets_with_valid_key(filter=''):
    """Тест на получение списка питомцев"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0
    print(f'\nstatus_code is - {status}')
# --------------------------------------------------------------------------------------------------------


def test_add_new_pet_with_valid_data(name=add_name, animal_type=add_animal_type, age=add_age, pet_photo=add_pet_photo):
    """Тест добавления питомца с корректными данными"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)  # Получаем полный путь изображения питомца и
    # сохраняем в переменную pet_photo

    _, auth_key = pf.get_api_key(valid_email, valid_password)  # Запрашиваем ключ api и сохраняем в переменную auth_key

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)  # Добавляем питомца
    assert status == 200
    assert result['name'] == name
    print(f'\nstatus_code is - {status}')
# ---------------------------------------------------------------------------------------------------------


def test_successful_update_self_pet_info(name=update_name, animal_type=update_animal_type, age=update_age):
    """Тест на обновления информации о питомце"""

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
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")
    print(f'\nstatus_code is - {status}')
# --------------------------------------------------------------------------------------------------------


def test_delete_pet_valid_user():
    """Тест на удаление питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Василий", "Python", "10", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()
    print(f'\nstatus_code is - {status}')
# ---------------------------------------------------------------------------------------------------------
