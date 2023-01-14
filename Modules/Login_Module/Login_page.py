from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()


class Login():
    usernamexpath = '//*[@name="username"]'
    passwordxpath = '//*[@name="password"]'
    loginbuttonxpath = '//*[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]'
    Loginbutton = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, loginbuttonxpath)))
    driver.find_element(By.XPATH,usernamexpath).send_keys('Admin')
    driver.find_element(By.XPATH,passwordxpath).send_keys('admin123')
    driver.find_element(By.XPATH,loginbuttonxpath).click()




