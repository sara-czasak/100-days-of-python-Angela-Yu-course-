from ssl import Options

from selenium import webdriver
from selenium.webdriver.common.by import By


# Constants
COOKIE_CLICKER_URL ='https://ozh.github.io/cookieclicker/'


# Set up chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)


# Get cookie clicker page
driver.get(COOKIE_CLICKER_URL)



# Close page once done
driver.quit()