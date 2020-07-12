import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chromeOptions = Options()
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("test-type")
chromeOptions.add_argument("enable-strict-powerful-feature-restrictions")
chromeOptions.add_argument("enable-geolocation")
cap = chromeOptions.to_capabilities()

driver = webdriver.Chrome('chromedriver.exe', options=chromeOptions, desired_capabilities=cap)
driver.get('https://tinder.com')

beginClose = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/button')))
# beginClose.click()
loginButton = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')))
# loginButton.click()
loginViaFB = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')))
# loginViaFB.click()
try:
    loginViaFB.click()
except Exception:
    try:
        beginClose.click()
        loginButton.click()
        loginViaFB.click()
    except Exception:
        pass
baseWindow = driver.window_handles[0]
fbPopup = driver.switch_to.window(driver.window_handles[1])

emailInput = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
pwdInput = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pass"]')))
submitLogin = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="u_0_0"]')))
emailInput.send_keys('email ')
pwdInput.send_keys('password')
submitLogin.click()
driver.switch_to.window(driver.window_handles[0])
location = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')))

location.click()
notiffications = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')))
notiffications.click()
likeButton = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')))
dislikeButton = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')))
x=1
while True:
    try:
        likeButton.click()
        time.sleep(0.3)
        print('Like no. ' + str(x))
        x+=1
    except Exception:
        try:
            startScreen = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div[2]/button[2]')))
            startScreen.click()
        except Exception:
            pass

driver.close()