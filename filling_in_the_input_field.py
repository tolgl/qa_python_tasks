import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Найди поле "Email" и заполни его
driver.find_element(By.ID, 'email').send_keys('glinkin@bigam.ru')

# Найди поле "Пароль" и заполни его
driver.find_element(By.ID, 'password').send_keys('Veropharm1997!')

# Найди кнопку "Войти" и кликни по ней
driver.find_element(By.XPATH, './/button[@class = "auth-form__button"]').click()

# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'header__user')))

# Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
assert driver.current_url == 'https://qa-mesto.praktikum-services.ru/'

driver.quit()
