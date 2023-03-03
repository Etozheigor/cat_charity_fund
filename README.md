# Cat Charity Fund
### О проекте
Cat Charity Fund - API-сервис для благотворительного фонда поддержки котиков. Администраторами фонда создаются 
целевые проекты для сбора средств, а пользователи могут делать пожертвования. Пожертвования делаются не на кокретный проект, а в фонд в целом. Все пожертвования идут в проект, открытый раньше других, после сбора нужной суммы проект закрывается и пожертвования начинают поступать в следующий проект.


### Технологии
В данном проекте я отвечал за бэкенд-часть и использовал следующие технологии:
- Python
- FastAPI
- Alembic
- SQLAlchemy
- Uvicorn



### Как запустить проект:

- Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Etozheigor/cat_charity_fund.git
```

```
cd cat_charity_fund
```

- Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

- Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

- создать файл .env и заполнить его по шаблону:

```
touch .env
```

шаблон заполнения env-файла:

```
DATABASE_URL=описание подключения к базе данных, по умолчанию в проекте стоит база данных sqlite+aiosqlite:///./fastapi.db, вы можете установить свою
SEKRET=ваш секретный ключ
```

- Выполнить миграции:

```
alembic init
```
```
alembic upgrade head
```

- Запустить проект:

```
uvicorn app.main:app
```

Проект будет доступен локально по адресу:

```
http://127.0.0.1:8000/
```

Эндпоинт с документацией swagger, через который можно делать запросы:
```
http://127.0.0.1:8000/docs
```





