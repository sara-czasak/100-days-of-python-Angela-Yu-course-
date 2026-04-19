from selenium import webdriver
from selenium.webdriver.common.by import By


# prevent browser window from closing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Set up driver
driver = webdriver.Chrome(options=chrome_options)

driver.get(url='https://www.python.org/')


# Find all upcoming events
# Get menu of all events
menu = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')

dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
events = driver.find_elements(By.CSS_SELECTOR, '.event-widget .menu a')

event_dict = {}

for i in range(5):
    event_dict[i] = {
        'event': events[i].text,
        'date': dates[i].text
    }

print(event_dict)


driver.quit() # Close pages after your done