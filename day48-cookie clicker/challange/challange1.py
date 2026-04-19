from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


URL = 'https://secure-retreat-92358.herokuapp.com/'

# prevent browser window from closing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Set up driver
driver = webdriver.Chrome(options=chrome_options)

driver.get(url=URL)

fname = driver.find_element(By.NAME, 'fName')
fname.send_keys('Sara')

lname = driver.find_element(By.NAME, 'lName')
lname.send_keys('Czasak')

email = driver.find_element(By.NAME, 'email')
email.send_keys('rainbowsperler@gmail.com')

sign_up_button = driver.find_element(By.XPATH, '/html/body/form/button')
sign_up_button.click()

driver.quit()