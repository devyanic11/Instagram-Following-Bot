from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time

USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"

chrome_driver_path = "YOUR CHROMEDRIVER PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.instagram.com/caught_n_posted_8088/")

log_in = WebDriverWait(driver, timeout=60).until(lambda d: d.find_element(By.CSS_SELECTOR, 'a button'))
log_in.click()

time.sleep(10)
username = WebDriverWait(driver, timeout=60).until(lambda d: d.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
username.send_keys(USERNAME)
password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys(PASSWORD)
time.sleep(2)
enter = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
enter.click()

time.sleep(15)
not_now = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element(By.CSS_SELECTOR, '._ac8f button'))
not_now.click()

#To click on Followers List
time.sleep(10)
followers = WebDriverWait(driver, timeout=60).until(lambda d: d.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a'))
followers.click()

#To Click on Follow Button in Popup(Not Working)
buttons = WebDriverWait(driver, timeout=60).until(lambda d: d.find_elements(By.TAG_NAME, 'button'))
for btn in buttons:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    
#To Scroll in Popup
# scr1 = WebDriverWait(driver, timeout=60).until(lambda d: d.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]'))
# while True:
#     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
