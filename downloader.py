import subprocess

# Function to install dependencies
def install_dependencies():
    try:
        subprocess.run(["pip", "install", "requests"])
        subprocess.run(["pip", "install", "selenium"])
        # Add any other dependencies you may need

        print("Dependencies installed successfully.")
    except Exception as e:
        print(f"Error installing dependencies: {e}")

# Function to download chromedriver
def download_chromedriver():
    try:
        subprocess.run(["wget", "https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip"])
        subprocess.run(["unzip", "chromedriver_linux64.zip"])
        subprocess.run(["mv", "chromedriver", "/usr/local/bin/"])

        print("Chromedriver downloaded and moved to /usr/local/bin/")
    except Exception as e:
        print(f"Error downloading Chromedriver: {e}")

# Install dependencies
install_dependencies()

# Download and move chromedriver
download_chromedriver()


import time
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

def random_sleep():
    time.sleep(random.uniform(15, 20))  # Adjust the sleep range as needed

def get_proxies():
    response = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')
    return response.text.strip().split('\n')

def test_proxy(proxy):
    if not proxy.startswith(('http://', 'https://')):
        proxy = 'http://' + proxy
    try:
        response = requests.get('http://www.example.com', proxies={'http': proxy, 'https': proxy}, timeout=10)
        response.raise_for_status()
        print(f"Proxy {proxy} is working.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error testing proxy {proxy}: {e}")
        return False


def set_proxy(proxy):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--proxy-server={proxy}')
    chrome_options.set_page_load_timeout(30)

    return webdriver.Chrome(options=chrome_options)

def main():
    all_proxies = get_proxies()
    
    for proxy in all_proxies:
        try:
            myproxy = test_proxy(proxy)
            if myproxy == True:
                print(f'Proxy {proxy} is working.')
            else:
                continue
        except:
            continue
        if test_proxy(proxy):
            driver = set_proxy(proxy)

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
            break  # Exit the loop after the first successful run
        else:
            continue  # Move on to the next proxy

if __name__ == "__main__":
    main()
