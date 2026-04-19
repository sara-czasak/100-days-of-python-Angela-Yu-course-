from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

# Constants
COOKIE_CLICKER_URL ='https://ozh.github.io/cookieclicker/'


# Set up chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)


# Get cookie clicker page
driver.get(COOKIE_CLICKER_URL)

time.sleep(2)

select_language = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
select_language.click()

time.sleep(2)


cookie = driver.find_element(By.ID, 'bigCookie')

item_ids = [f'product{i}' for i in range(18)]

wait_time = 5
timeout = time.time() + wait_time
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:
        products = driver.find_elements(By.CSS_SELECTOR, "div[id^='product']")

        best_item = None
        for product in products[::-1]:
            if 'enabled' in product.get_attribute('class'):
                best_item = product
                break

        if best_item:
            best_item.click()

        timeout = time.time() + wait_time

    if time.time() > five_min:
        try:
            cookie_element = driver.find_element(By.ID, 'cookies')
            print(f"Final cookie crumble: {cookie_element.text}")
        except NoSuchElementException:
            print("sorry cookie monster stole all your cookies..")
        break




# Close page once done
driver.quit()