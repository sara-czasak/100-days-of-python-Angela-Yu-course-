from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By





# prevent browser window from closing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Set up driver
driver = webdriver.Chrome(options=chrome_options)

driver.get(url='https://www.python.org/')

# price_whole = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
# price_fraction = driver.find_element(By.CLASS_NAME, 'a-price-fraction').text

# print(f"The price is {price_whole}.{price_fraction}zł")

# search_bar = driver.find_element(By.NAME, 'q')
# search_bar.send_keys('Selenium')
# search_bar.send_keys(Keys.ENTER)
# button = driver.find_element(By.NAME, 'submit')
# docs = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
# print(docs.text)

# Find element by Xpath
# bug_website = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a').get_attribute('href')



driver.quit() # Close all browser windows
# driver.close() # Closes one tab