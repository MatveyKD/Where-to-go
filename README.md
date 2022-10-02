# Where-to-go
Сайт с интересными местами по Москве. Работающий сайт - [https://matvey257.pythonanywhere.com](https://matvey257.pythonanywhere.com).

## Как установить
- Скачайте код
- Установить зависимости командой `pip install -r requirements.txt`

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл .env рядом с manage.py и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение. [Документация](https://docs.djangoproject.com/en/4.1/ref/settings/)

Доступны 4 переменные:

- DEBUG — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- SECRET_KEY — секретный ключ проекта
- ALLOWED_HOSTS — см документацию Django
- DB_NAME - имя файла базы данных
- DB_ENGINE - движок базы данных

## Как запустить

- Создайте базу данных SQLite командой `python3 manage.py migrate`
- Создайте суперпользователя командой `python manage.py createsuperuser`
- Запустите командой `python manage.py runserver`

## Как зарузить данные
Чтобы загрузить данные из json файла, используйте management-команду `load_place`

    $ python manage.py load_place places/place.json

Чтобы загрузить все файлы из папки, используйте аргумент -d:

    $ python manage.py load_place places/place.json -d True

Чтобы загрузить файл по ссылке, используйте аргумент -u:

    $ python manage.py load_place -u https://places.com/place.json