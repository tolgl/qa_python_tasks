import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Выполни авторизацию
driver.find_element(By.ID, 'email').send_keys('glinkin@bigam.ru')
driver.find_element(By.ID, 'password').send_keys('Veropharm1997!')
driver.find_element(By.CLASS_NAME, 'auth-form__button').click()

# Добавь явное ожидание для загрузки списка карточек контента
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'places__list')))

# Запомни title последней карточки
title_before = driver.find_element(By.XPATH, ".//li[@class = 'places__item card']//h2[@class = 'card__title']").text

# Кликни по кнопке добавления нового контента
driver.find_element(By.CLASS_NAME, 'profile__add-button').click()

# сгенерируй новое место и введи его в поле названия
new_title = f'Москва{random.randint(100,999)}'
driver.find_element(By.ID, 'place-name').send_keys(new_title)

# В поле ссылки на изображение введи ссылку
driver.find_element(By.ID, 'place-link').send_keys('https://code.s3.yandex.net/qa-automation-engineer/python/files/photoSelenium.jpeg')

# Сохрани контент
driver.find_element(By.XPATH, ".//form[@name = 'new-card']/button[text() = 'Сохранить']").click()

# Дождись появления кнопки удаления карточки
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//section[2]//li[@class = 'places__item card'][1]/button[@class = 'card__delete-button card__delete-button_visible']")))
# Проверь, что на карточке отображается верное название
title_after = driver.find_element(By.XPATH, ".//li[@class = 'places__item card']//h2[@class = 'card__title']").text
print(title_after)
assert title_after == new_title

# Запомни количество карточек до удаления
cards_before = len(driver.find_elements(By.XPATH, ".//li[@class = 'places__item card']"))
print(cards_before)

# Удали карточку
driver.find_element(By.XPATH, ".//section[2]//li[@class = 'places__item card'][1]/button[@class = 'card__delete-button card__delete-button_visible']").click()

# Дождись, что title последней карточки равен title_before
WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']"), title_before))

# Проверь, что количество карточек стало на одну меньше
cards_after = len(driver.find_elements(By.XPATH, ".//li[@class = 'places__item card']"))
print(cards_after)
assert cards_after == cards_before - 1

driver.quit()
