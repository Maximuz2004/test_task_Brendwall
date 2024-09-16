# test_task_Brendwall
Тестовое задание для собеседования в компанию "Brendwall"

## Используемые технологии: 
![Python3](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Django5](https://img.shields.io/badge/Django-5.x-green?logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-3.x-blue?logo=django&logoColor=white)
![drf-yasg](https://img.shields.io/badge/drf--yasg-1.21.7-green?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3.x-blue?logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.x-purple?logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-black?logo=javascript&logoColor=white)


## Описание

Этот проект является тестовым заданием для компании Brendwall. Небольшое 
Django-приложение, которое добавляет данные о продуктах в БД и возвращает 
их список.

## Функциональность

- Создано DRF- API для работы с продуктами (создание и получение списка).
- Создана страница на HTML с использованием JavaScript для отправки данных на 
API и отображения продуктов.

## Установка

Следуйте этим шагам, чтобы установить проект на ваш локальный компьютер:

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/Maximuz2004/test_task_Brendwall.git
   ```
2. Перейдите в директорию проекта:

    ```bash
    cd test_task_Brendwall
    ```
3. Подготовьте виртуальное окружение и активируйте его. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Выполните миграции:
   ```python
   python manage.py makemigrations
   python manage.py migrate
   ```

## Запуск
Чтобы запустить проект:
   ```python
   python3 manage.py runserver
   ```

### Доступные эндпоинты:
|  Эндпойнт | Методы  | Описание                                      |
|--|--|-----------------------------------------------|
| ```.../api/products/create/``` | ``` POST ``` | Добавление названия продукта, описания и цены |
| ```.../api/products/list/``` | ``` GET ``` | Получение всех продуктов  из БД               |

### Страница с формой 
для добавления нового продукта (поля: название, описание, цена) и кнопкой "Отправить"

`GET .../api/products/`
## Документация

Проект включает в себя документацию, доступную через следующие инструменты:

- **Swagger**: Документация для вашего API доступна через ```.../swagger/```.
- **Redoc**: Альтернативная версия документации доступна через ```.../redoc/```.



### Автор
[Максим Титов](https://github.com/Maximuz2004)