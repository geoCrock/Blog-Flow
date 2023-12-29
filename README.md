# Blog-Flow
Тестовое задание для компании "ЦИСМ"

Комментарии: 

Теперь есть тестовый `.env` файл.

Весь сайт теперь на русском.

Добавлена возможность регестрации пользователей, а так же: лайк может ставить только 1 раз 1 пользователь(при нажатии второй раз лайк отменяется),
редактировать и удалять посты может только создавший пользователь, появилась возможность выйти из аккаунта.

Миграции происходят внутри контейнера.

## Описание
BlogFlow - это удобный и интуитивно понятный веб-портал, предназначенный для творческих личностей, желающих делиться своими мыслями и идеями с миром. Наш проект предоставляет простой и эффективный инструмент для создания, редактирования и управления вашими блоговыми постами.

Особенности:

- Создание постов: Интуитивная форма создания постов, которая позволяет вам свободно выражать свои мысли и идеи.
- Редактирование постов: Возможность вносить изменения в уже опубликованные посты, сохраняя актуальность контента.
- Управление постами: Простой интерфейс для управления вашими постами, включая удаление, редактирование и отслеживание статистики.
- Лайки и обратная связь: Возможность получать обратную связь от читателей в виде лайков и комментариев.
- Blog-Flow создан для того, чтобы ваш творческий поток не прерывался. Делитесь своими историями, мнениями и впечатлениями с миром, используя BlogFlow - ваш идеальный партнер в блоггинге.

## Запуск

1. Скопируйте репозиторий:

     ```bash
     git clone https://github.com/geoCrock/Blog-Flow.git
     ```

2.  Cоздайте `venv` и установите зависимости:

     ```bash
     python -m venv venv
     ```
     или

     ```bash
     source venv/bin/activate
     ```
     
     ```bash
     pip install -r requirements.txt
     ```

3. Сделайте миграции и запустите проект:
   
    ```bash
    python manage.py makemigrations
     ```

    ```bash
    python manage.py migrate
     ```

    ```bash
    python manage.py runserver
     ```


##  Запуск через Docker

Убедитесь, что в вашей системе установлены следующие компоненты:

- Docker
- Docker Compose


1. Скопируйте репозиторий:

     ```bash
     git clone https://github.com/geoCrock/Blog-Flow.git
     ```

2. Создайте и запустите контейнеры Docker:

     ```bash
     docker-compose up --build
     ```
