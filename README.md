# Скрипт для получения последних твитов Илона Маска из Twitter

Этот скрипт использует Selenium для автоматизации прокрутки страницы Илона Маска в Twitter и получения последних 10 твитов.

## Использование
1. Установите необходимые зависимости, запустив команду `pip install selenium`.
2. Установите Chrome WebDriver.
3. Замените значение переменной `proxy` на ваш прокси-сервер, если требуется.
4. Запустите скрипт командой `python redmi.py`.

## Описание кода
- Функция `check_tweet_count` проверяет, что на странице присутствует 10 или более твитов.
- Создается экземпляр драйвера Chrome с настройками прокси.
- Скрипт переходит на страницу Илона Маска в Twitter.
- Происходит прокрутка страницы вниз до тех пор, пока количество твитов не превысит 10.
- Получение текста последних 10 твитов и вывод их в консоль.
- Браузер закрывается после выполнения скрипта.


# Скрипт для сбора данных о фондовом рынке из NSE India

Этот скрипт использует Selenium для сбора данных о фондовом рынке с веб-сайта NSE India.

## Использование
1. Установите необходимые зависимости, запустив команду `pip install selenium`.
2. Установите Chrome WebDriver. 
3. Запустите скрипт командой `python <имя_скрипта>.py`.

## Описание кода
- Функция `parse_final_prices` открывает веб-сайт NSE India, переходит в раздел Pre-Open Market и получает названия и конечные цены акций. Данные сохраняются в CSV файл с именем `final_prise.csv`.
- Функция `execute_user_scenario` открывает веб-сайт NSE India, переходит в раздел NIFTY BANK и выполняет различные действия для имитации сценария пользователя.
- Основной код вызывает функции `parse_final_prices` и `execute_user_scenario`.

## Зависимости
- Selenium (`pip install selenium`)
