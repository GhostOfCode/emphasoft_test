# Тестовое задание для EmphaSoft

## Описание задания
Веб приложение на Django. <br>
При открытии приложение показывает кнопку «авторизоваться», по нажатию делает oauth авторизацию ВКонтакте,
показывает имя авторизованного пользователя и 5 любых друзей пользователя.<br>
При последующих запусках/заходах на страницу сразу показывает всю информацию т.к. уже понимает,
что пользователь авторизован.

## Настройки программы
Для успешной работы веб приложения:
1. [Создайте приложение vk]

1. Скопируйте содержимое settings.py.default в settings.py <br>
`cp emphasoft_test/emphasoft_test/settings.py.default emphasoft_test/emphasoft_test/settings.py`

1. Добавить ID приложения, Защищённый ключ и секретный ключ django приложения в settings.py

1. Создайте и активируйте виртуальное окружение: <br>
`virtualenv venv` <br>
`source venv/bin/activate`

1. Установите пакеты из requirements.txt: <br>
`pip install -p requirements.txt`

1. Сделайте миграцию приложения: <br>
`./emphasoft_test/manage.py migrate`

## Запуск веб-приложения
`./emphasoft_test/manage.py runserver`

[Создайте приложение vk]: https://vk.com/editapp?act=create
