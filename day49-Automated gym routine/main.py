from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import os


# CONSTANTS
URL ='https://appbrewery.github.io/gym/'
test_email = 'rainbowsperler@gmail.com'
test_password = 'Mypass123456word'


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
# user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
# chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)



driver.get(URL)


time.sleep(3)
login_button = driver.find_element(By.ID, 'login-button')
login_button.click()
time.sleep(3)
email_input = driver.find_element(By.ID, 'email-input')
email_input.send_keys(test_email)
password_input = driver.find_element(By.ID, 'password-input')
password_input.send_keys(test_password)
submit_button = driver.find_element(By.ID, 'submit-button')
submit_button.click()



# driver.quit()