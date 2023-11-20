from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# здесь добавь свой предыдущий код для добавления куки
new_cookie = {'name': 'my_first_cookie', 'value': '15'}
driver.add_cookie(new_cookie)

# а теперь измени значение куки
driver.delete_cookie('my_first_cookie')

new_cookie = {'name': 'my_first_cookie', 'value': '25'}
driver.add_cookie(new_cookie)

# Проверь новое значение поля value для добавленной куки
cookie = driver.get_cookie('my_first_cookie')
print(cookie['value'])
assert cookie['value'] == '25'

driver.quit()
