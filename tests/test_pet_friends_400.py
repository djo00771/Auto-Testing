from api import PetFriends
from settings import *
import os


pf = PetFriends()


def test_get_api_key_for_non_mail_and_pass(email='', password=''):
    """ Проверяем что запрос api ключа возвращает статус 403. Если нет email и password """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert "This user wasn't found in database" in result
    print(f'\nstatus_code is - {status}')
# -----------------------------------------------------------------------------------------------------


def test_get_api_key_for_invalid_mail(email=invalid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 403. Если email не верный """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert "This user wasn't found in database" in result
    print(f'\nstatus_code is - {status}')
# -----------------------------------------------------------------------------------------------------


def test_get_api_key_for_invalid_pass(email=valid_email, password=invalid_password):
    """ Проверяем что запрос api ключа возвращает статус 403. Если password не верный"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert "This user wasn't found in database" in result
    print(f'\nstatus_code is - {status}')
# -----------------------------------------------------------------------------------------------------


def test_add_new_pet_with_invalid_key_and_error_data(name=add_name, animal_type=add_animal_type,
                                     age=add_age, pet_photo=add_pet_photo):
    """Проверяем что добавить питомца с корректными данными и неверным ключом нельзя"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)  # Запрашиваем ключ api и сохраняем в переменную auth_key

    # Пробуем добавить питомца
    status, result = pf.add_new_pet(invalid_auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403
    assert "Please provide 'auth_key'" in result
    print(f'\nstatus_code is - {status}')
# -----------------------------------------------------------------------------------------------------


def test_add_new_pet_with_rotten_key(name=add_name, animal_type=add_animal_type,
                                     age=add_age, pet_photo=add_pet_photo):
    """Проверяем что добавить питомца с корректными данными и ключом с истекшим сроком нельзя"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Пробуем добавить питомца
    status, result = pf.add_new_pet(rotten_auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403
    assert "Please provide 'auth_key'" in result
    print(f'\nstatus_code is - {status}')
# -----------------------------------------------------------------------------------------------------
