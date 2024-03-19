from bs4 import BeautifulSoup
from requests_html import HTMLSession

# Создание объекта сеанса
session = HTMLSession(browser_args=["--proxy-server=86.48.0.127:3128"])

# URL прокси сервера
proxy_url = 'http://86.48.0.127:3128'

# Настройка прокси
proxies = {
    'http': proxy_url,
    'https': proxy_url
}

# Запрос на получение содержимого веб-страницы с использованием прокси
response = session.get('https://twitter.com/elonmusk', proxies=proxies)

# Рендеринг страницы для получения полного HTML-кода
response.html.render(scrolldown=8, sleep=10)

# Создание объекта BeautifulSoup для парсинга HTML-кода
soup = BeautifulSoup(response.html.html, 'html.parser')

# Поиск всех твитов на странице
tweets = soup.find_all('div', attrs={'data-testid': 'cellInnerDiv'})[:10]
for tweet in tweets:
    try:
        # Поиск текста твита и его вывод
        tweet_text = tweet.find('div', attrs={'data-testid': 'tweetText'})
        print(tweet_text.text)
    except:
        print("Нет текста")
