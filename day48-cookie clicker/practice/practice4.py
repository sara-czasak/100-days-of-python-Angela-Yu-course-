from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


# prevent browser window from closing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Set up driver
driver = webdriver.Chrome(options=chrome_options)

driver.get(url='https://en.wikipedia.org/wiki/Main_Page')

# Get number of articles in english
# articles_in_english = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')

# print(articles_in_english.text)
# articles_in_english.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

search_button = driver.find_element(By.XPATH, '//*[@id="p-search"]/a/span[1]')
search_button.click()

time.sleep(3)

search_bar = driver.find_element(By.XPATH, '//*[@id="searchform"]/div/div/div[1]/input')

search_bar.send_keys('Python')
search_bar.send_keys(Keys.ENTER)
# submit_button = driver.find_element(By.XPATH, '//*[@id="searchform"]/div/button')
# submit_button.click()

time.sleep(3)

python_language = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[2]/ul[2]/li[1]/a')
python_language.click()

time.sleep(3)

first_p = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[2]/p[2]')

print(first_p.text)

driver.quit()