# Сайт риэлторского агентства

Сайт находится в разработке, поэтому доступна только страница со списком квартир и админка для наполнения БД.

 [Демка сайта](http://foxhole.pythonanywhere.com/)

## Запуск

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных и сразу примените все миграции командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE` — строка подключения к базе данных, например: `sqlite:///db.sqlite3`. Больше информации в [документации](https://github.com/jacobian/dj-database-url)

    Это позволяет легко переключаться между базами данных: PostgreSQL, MySQL, SQLite — без разницы, нужно лишь указать строку подключения

## Соединение с СУБД

#### Есть два  варианта:

1. SQLlite + django ORM - На ветке main с использвоанием локальной БД и ORM Django

2. PostgreSQL + psycopg2 - На ветке postgresql с использованием адаптера и выполнением прямых SQL запросов.
