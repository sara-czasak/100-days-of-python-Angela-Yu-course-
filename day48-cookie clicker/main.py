from selenium import webdriver


# Constants
COOKIE_CLICKER_URL ='https://ozh.github.io/cookieclicker/'


# prevent browser window from closing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Set up driver
driver = webdriver.Chrome(options=chrome_options)

driver.get(COOKIE_CLICKER_URL)


driver.quit() # Close all browser windows
# driver.close() # Closes one tab