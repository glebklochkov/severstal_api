# Tasks REST API

Простой REST API с задачами, реализованный на Django REST Framework.

## Функциональность

Реализованы следующие возможности:
- создание новой задачи
- получение списка всех задач
- получение одной задачи по идентификатору
- фильтрация задач по статусу
- сортировка задач по id и названию

## Модель Task

Модель Task имеет следующие поля:
- 'id' - уникальный идентификатор
- 'title' - название задачи
- 'description' - описание задачи (необязательное)
- 'status' - статус задачи active/completed (по умолчанию ставится active)

## API Эндпоинты

- **POST** `/api/tasks/` - создание задачи
- **GET** `/api/tasks/` - получение списка задач
- **GET** `/api/tasks/<id>/` - получение задачи по id
- **GET** `/api/tasks/?status=active` - фильтрация задач по статусу
- **GET** `/api/tasks/?ordering=title` - сортировка задач

## Установка и запуск проекта

- `git clone <repository_url>`
- `cd <project_directory>`
- `python -m venv venv`
- `venv\Scripts\activate`
- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`
