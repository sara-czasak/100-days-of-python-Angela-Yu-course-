from selenium import webdriver
from selenium.webdriver.common.by import By


# prevent browser window from closing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Set up driver
driver = webdriver.Chrome(options=chrome_options)

driver.get(url='https://en.wikipedia.org/wiki/Main_Page')



driver.quit()