import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = "https://www.saucedemo.com/"

# добавить опции
options = webdriver.ChromeOptions()

# оставить браузер открытым
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере
driver_chrome.get(base_url)

# команда для открытия окна в максимальном для монитора разрешении
driver_chrome.maximize_window()

# найти на странице элемент под id "user-name"
user_name = driver_chrome.find_element(By.ID, "user-name")

# пауза 2 секунды
time.sleep(2)

# установить в поле значение "standard_user"
user_name.send_keys("standard_user")
print("Ввод логина.")

# найти на странице элемент под id "password"
password = driver_chrome.find_element(By.ID, "password")

# пауза 2 секунды
time.sleep(2)

# установить в поле значение "secret_sauce"
password.send_keys("secret_sauce")
print("Ввод пароля.")

# пауза 2 секунды
time.sleep(2)

# найти на странице элемент под id "login-button"
login_button = driver_chrome.find_element(By.ID, "login-button")
# нажать на кнопку
login_button.click()
print("Нажатие на кнопку Login.")

# пауза 2 секунды
time.sleep(2)

# получение актуальных даты и времени
now_date = datetime.now().strftime("%Y.%m.%d-%H.%M.%S")

# новое имя для скриншота
name_screenshot = f"screenshot_{now_date}.png"

# сохранение скриншота
driver_chrome.save_screenshot(
    f"C:\\!!!вставить путь до папки!!!\\screenshots\\{name_screenshot}"
)
print(f"Скриншот \"{name_screenshot}\" сохранен.")

# закрыть окно браузера
driver_chrome.close()
print("Окно закрыто.")
