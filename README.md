# Note_system

### Описание 
Note_system - система для отправки уведомлений пользователям (учебный проект).

### Как запустить проект

Клонировать репозиторий:

```
git@github.com:mbragins1988/note_system.git  
```

Перейти в папку note_system:

```
cd note_system
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```
для Windows:
```
source venv/Scripts/activate
```
для Mac:
```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip3 install -r requirements.txt
```

В директории note_system выполнить миграции:

```
python manage.py makemigrations
```
```
python manage.py migrate
```

Создать суперпользовател:

```
python manage.py createsuperuser
```

Запустить сервер:

```
python manage.py runserver  
```

В админ-панели http://127.0.0.1:8000/admin добавить информацию о пользователе.


Проверка на примере Postman:

```
Укажите URL: http://localhost:8000/api/notifications/  
```
```
Выберите POST-запрос
```
```
Выберите "Body" -> "raw" -> "JSON"  
```
```
Вставьте
{
    "user": 1,
    "subject": "Test",
    "message": "Hello!"
} 
```

### Стек технологий:
- Python 3.8.10
- django 4.2.23
- djangorestframework 3.15.2

### Авторы проекта
Михаил Брагин



