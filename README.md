# Знакомство с Django: ORM «Пишем пульт охраны банка»

Учебный проект курса "От джуна до мидла" компании Devman. 

Использованная технология - Django ORM


## Задание

Бухгалтер Валентин работает в банке уже 15 лет. И он точно знает: лучший способ предотвращать финансовые потери – внимательно следить за сотрудниками и их операциями. Однако руководство банка не слушало Валентина и инвестировало в бугаев-охранников…

Пока однажды утром не обнаружило в хранилище недостачу $2 млн при полном отсутствии признаков ограбления. Сразу после этого Валентина выслушали очень внимательно и решили по его просьбе внедрить правила посещения хранилища.

Теперь перед входом в хранилище стоит пропускной пункт, а в базе данных фиксируются все посещения. Осталось только сделать пульт управления для охранника, чтобы он мог следить за всеми, кто там находится.

Дело за малым – выполнить заказ банка на пульт охраны. За работу!

    Подключимся к базе данных
    Отправим несколько запросов
    Выведем данные на сайте



## Установка и запуск

1. Клонируйте данный репозиторий на локальный компьютер.
```
git clone https://github.com/IBA20/django-orm-watching-storage
```
2. Создайте виртуальное окружение и установите зависимости
```
pip install -r requirements.txt
```
3. В корне проекта создайте файл .env со следующим содержимым:
```
SECRET_KEY=secretvalue
DEBUG=True
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
```
Параметры для подключения к БД - USER, PASSWORD, HOST, PORT, NAME - узнайте в своем личном кабинете Devman. Значеие секретного ключа для локального тестирования можно оставить как есть.  

5. Запустите сервер командой
```
python manage.py runserver
```


## Использование

1. Главная страница со списком активных пропусков находится по адресу http://localhost:8000/
2. Клик по любому из имен открывает список визитов данного посетителя в хранилище.
3. Список посетителей в хранилище в данный момент - по адресу http://localhost:8000/storage_information

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

