from selenium import webdriver
import time

# инициализируем драйвер браузера
driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")
# сделаем паузу
time.sleep(5)

# закроем браузер
driver.quit()
