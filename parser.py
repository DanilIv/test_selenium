import csv
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


def parse_final_prices():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.nseindia.com/")
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState ') == "complete")
    market_data = driver.find_element(By.LINK_TEXT, 'MARKET DATA')
    ActionChains(driver).move_to_element(market_data).perform()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, 'Pre-Open Market').click()

    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == "complete")

    time.sleep(3)

    name_element = driver.find_elements(By.XPATH, '//*[@id="livePreTable"]/tbody/tr/td[2]')
    final_prise_element = driver.find_elements(By.XPATH, '//*[@id="livePreTable"]/tbody/tr/td[7]')
    with open('final_prise.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Final prise'])

        for index in range(len(name_element) - 1):
            writer.writerow([name_element[index].text, final_prise_element[index].text])

    driver.quit()


def execute_user_scenario():

    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.nseindia.com/")
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState ') == "complete")
    chart = driver.find_element(By.ID, 'tab1_container')

    driver.execute_script("arguments[0].scrollIntoView();", chart)
    time.sleep(2)
    element=driver.find_element(By.ID, 'tabList_NIFTYBANK')
    action = ActionChains(driver)
    action.move_to_element(element).move_by_offset(element.size['width'] / 2,
                                                   element.size['height'] / 2).click().perform()
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState ') == "complete")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="tab4_gainers_loosers"]/div[3]/a').click()
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState ') == "complete")
    time.sleep(3)
    driver.find_element(By.ID, 'equitieStockSelect').click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//option[text()='NIFTY ALPHA 50']").click()
    time.sleep(10)

    # Пролистать таблицу до конца
    time.sleep(3)
    table = driver.find_element(By.ID, 'equityStockTable')
    table_tr = table.find_elements(By.XPATH, './/tbody/tr')

    # Проскролить таблицу до последнего tr
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", table_tr[-2])
    time.sleep(3)

if __name__ == '__main__':
    parse_final_prices()
    execute_user_scenario()
