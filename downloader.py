import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

def random_sleep():
    time.sleep(random.uniform(15, 20))

# Set up the Selenium WebDriver (you need to specify the path to your webdriver)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Add other options if needed
chrome_options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.file-upload.org/gy4xwjd0ec4h'
driver.get(url)

random_sleep()

post_data_1 = {'op': 'download1', 'usr_login': '', 'id': 'gy4xwjd0ec4h', 'fname': 'aerial_rocks_02_disp_4k.png', 'referer': 'https://www.babup.com/', 'method_free': 'Free Download'}

try:
    response_1 = requests.post('https://www.file-upload.org/gy4xwjd0ec4h', data=post_data_1)
    response_1.raise_for_status()  # Check for HTTP errors
except requests.exceptions.RequestException as e:
    print(f'Error in the first POST request: {e}')
    driver.quit()
    continue  # Move on to the next proxy

try:
    form_f1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'F1'))
    )
    rand_value = form_f1.find_element(By.NAME, 'rand').get_attribute('value')
except Exception as e:
    print(f'Error locating form with name="F1": {e}')
    driver.quit()
    continue  # Move on to the next proxy

random_sleep()

post_data_2 = {'op': 'download2', 'id': 'gy4xwjd0ec4h', 'rand': rand_value, 'referer': 'https://www.babup.com/', 'method_free': 'Free Download', 'method_premium': '', 'g-recaptcha-response': 'YourCaptchaResponse', 'h-captcha-response': 'YourHCaptchaResponse'}

try:
    response_2 = requests.post('https://www.file-upload.org/gy4xwjd0ec4h', data=post_data_2)
    response_2.raise_for_status()  # Check for HTTP errors
except requests.exceptions.RequestException as e:
    print(f'Error in the second POST request: {e}')
    driver.quit()
    continue  # Move on to the next proxy

random_sleep()

try:
    element_id = 'download-btn'
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, element_id))
    )
    file_url = element.get_attribute('href')
except Exception as e:
    print(f'Error locating element with id="{element_id}": {e}')
    driver.quit()
    continue  # Move on to the next proxy

try:
    file_response = requests.get(file_url)
    file_response.raise_for_status()  # Check for HTTP errors
except requests.exceptions.RequestException as e:
    print(f'Error downloading the file: {e}')
    driver.quit()
    continue  # Move on to the next proxy

with open('downloaded_file.zip', 'wb') as file:
    file.write(file_response.content)

# Delete the downloaded file
os.remove('downloaded_file.zip')

driver.quit()
