import pytest
import requests


def test_calculate_total_post_body_length():
    """
    Тест для подсчета общей длины всех постов.

    Задание:
    1. Отправить GET-запрос на 'https://dummyjson.com/posts'.
    2. Подсчитать общую длину всех текстов (body) у постов.
    3. Проверить, что итоговая длина соответствует ожидаемому значению.

    В этом тесте есть несколько ошибок. Найдите и исправьте их.
    """
    response = requests.get("https://dummyjson.com/posts")

    total_length = 0
    # Ошибки спрятаны где-то здесь
    for post in response.json()['posts']:
        total_length += len(post['body'])

    # Это значение неверное, так как код подсчета работает неправильно
    expected_length = 4500
    assert total_length == expected_length, Exception(f"Ожидалось {expected_length}, но было получено {total_length}")
