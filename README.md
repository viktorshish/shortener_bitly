# Обрезка ссылок с помощью сервиса Битли
Shortener Bitly позволяет быстро из консоли, сократить вашу ссылку и получить информацию о количестве перходов по ней.

## Как установить
- Получите токен. Зарегестрируйтесь на [сайте](https://bitly.com), [генератор токенов](https://app.bitly.com/settings/api/). Токен выглядит наподобие такой строки: 17c09e20ad155405123ac1977542fecf00231da7 
- Создайте в корне проекта, файл ```.env``` 
Пропишите в нем:
```BITLY_TOKEN=ВАШ ТОКЕН```
- Для изоляции проекта рекомендуется развернуть виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
- Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

## Использование
- Получение короткой ссылки:
```
python main.py ВАША ССКА
```
![create link bitly](https://github.com/viktorshish/shortener_bitly/assets/108957333/3308f0ca-ea0a-466e-b9b7-2199e0425ffa)

- Получение информации о количестве преходов по Bitly ссылке:
```
python main.py BITLY ССЫЛКА
```
![info bitly link](https://github.com/viktorshish/shortener_bitly/assets/108957333/9449d061-673d-4b06-b047-e0cb42887471)

- Cправка:
```
pytthon main.py -h
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
