from selenium import webdriver
from selenium.webdriver.common.by import By


# prevent browser window from closing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Set up driver
driver = webdriver.Chrome(options=chrome_options)

driver.get(url='https://en.wikipedia.org/wiki/Main_Page')

# Get number of articles in english
# articles_in_english = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]').text
articles_in_english = driver.find_elements(By.CSS_SELECTOR, '#articlecount a')[1]
print(articles_in_english.text)

driver.quit()