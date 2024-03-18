import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

def check_tweet_count():
    # Проверка количества твитов
    return len(driver.find_elements(By.XPATH, '//div[@data-testid="cellInnerDiv"]')) >= 12

# Определение настроек для драйвера Selenium
proxy = "86.48.0.127:3128"
chrome_options = Options()
chrome_options.add_argument('--proxy-server=%s' % proxy)

# Инициализация драйвера Chrome с настройками прокси
driver = webdriver.Chrome(options=chrome_options)

# Переход на страницу Илона Маска в Twitter
driver.get("https://twitter.com/elonmusk")

# Скроллинг страницы вниз до появления больше 10 твитов
actions = ActionChains(driver)
while not check_tweet_count():
    try:
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)
    except TimeoutException:
        driver.refresh()  # Обновление страницы
        time.sleep(5)

tweets = driver.find_elements(By.XPATH, '//div[@data-testid="cellInnerDiv"]')[:10]

# Получение текста последних 10 твитов и вывод в лог
for tweet in tweets:
    try:
        tweet_text = tweet.find_element(By.XPATH, './/div[@data-testid="tweetText"]').text
        print(tweet_text)
    except NoSuchElementException:
        print("Нет текста")

# Закрытие браузера
driver.quit()
