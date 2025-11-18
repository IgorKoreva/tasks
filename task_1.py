
import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_user_posts_workflow():
    """
    Сценарий для проверки полного цикла работы с постами пользователя.

    Шаги:
    1. Создать нового пользователя (POST /users). Поля пользователя: name, username, email в формате str.
    2. Проверить, что пользователь успешно создан (статус-код 201).
    3. Создать новый пост для этого пользователя (POST /posts). Поля для поста: title, body в формате str, userId в формате int.
    4. Проверить, что пост успешно создан (статус-код 201).
    5. Получить список постов для данного пользователя (GET /users/{userId}/posts).
    6. Проверить, что созданный пост присутствует в списке постов пользователя.
    """
    # Создать нового пользователя (POST /users). Поля пользователя: name, username, email в формате str.
    # Проверить, что пользователь успешно создан (статус-код 201)
    res = requests.post('https://jsonplaceholder.typicode.com/users', json={
        'name': 'user909',
        'username': 'user_name',
        'email': '1@ya.ru'
    })
    assert res.status_code == 201, Exception('Статус не 201')
    user_id = res.json().get('id')

    # Создать новый пост для этого пользователя (POST /posts). Поля для поста: title, body в формате str,
    # userId в формате int. Проверить, что пост успешно создан (статус-код 201)
    res = requests.post('https://jsonplaceholder.typicode.com/posts', json={
        'title': 'название',
        'body': 'Тело статьи',
        'userId': user_id
    })
    assert res.status_code == 201, Exception('Статус не 201')
    post_id = res.json().get('id')

    # Получить список постов для данного пользователя (GET /users/{userId}/posts)
    res = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/posts/')
    posts_ids = list(x['id'] for x in res.json())
    assert post_id in posts_ids, Exception('Нет созданого поста в списке постов')


