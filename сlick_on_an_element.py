from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

driver.get("https://qa-mesto.praktikum-services.ru/")

# ожидаем пока элемент не станет активным
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, './/button[@class = "auth-form__button"]')))
# Найди кнопку и кликни по ней
driver.find_element(By.XPATH, './/button[@class = "auth-form__button"]').click()


driver.quit()
