import time
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

print(driver.capabilities['chrome']['chromedriverVersion'])


def random_sleep():
    
    time.sleep(random.uniform(16, 22))

# Set up the Selenium WebDriver (you need to specify the path to your webdriver)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Add other options if needed
driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.file-upload.org/gy4xwjd0ec4h'
driver.get(url)

random_sleep()

driver.get(url)

random_sleep()

post_data_1 = {'op': 'download1', 'usr_login': '', 'id': 'gy4xwjd0ec4h', 'fname': 'aerial_rocks_02_disp_4k.png', 'referer': 'https://www.babup.com/', 'method_free': 'Free+Download'}
response_1 = requests.post('https://www.file-upload.org/gy4xwjd0ec4h', data=post_data_1)

form_f1 = driver.find_element(By.ID, 'F1')
rand_value = form_f1.find_element(By.NAME, 'rand').get_attribute('value')

random_sleep()

post_data_2 = {'op': 'download2', 'id': 'gy4xwjd0ec4h', 'rand': rand_value, 'referer': 'https://www.babup.com/', 'method_free': 'Free Download', 'method_premium': '', 'g-recaptcha-response': 'P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hKdwYXNza2V5xQQjhox84v_tK8EPiufmBlxYH_KvXi9z2FBNmsAlXBt_JvFK-BsGWrzybBJS-mL1BvL63eaLkvQ-914hJJZ8hjGHH8M3idwPVGnkZROvSOoimFNAp9C0Ru8YE0Fb5MPMErECLCYBxLsX0Up4YVVcFH6TG_EetGYF4FUQF6LBhjWWZgqP3qjy0RFNcgTQ9S57yQZHjjuZwD4c-i0rhzBHnwjKbVW6KgYcKPNWXs5B7g8cNoYDKOXq3wUcbyxDV3hUXPwj3rojNK-oxxeV4p6hBWDqCAJEdFERORAYNoDtds4EtOOfDWb-ZhWDPs5KPXWje9-yupREMGrII4h4p-Wp4veb3Pa9mNHR08Qkxh1WivfGs97eOgdkO74nKCGSyIU4CMVxWuKB9nUfXQH2jFjhB2lszG9k9O8VcWldRyjD6h09HPYOClQRO3pW_EcQLtp8R-OGR7sM6S4jTcUh2ehdU-LMbTYjo_Q5nVxporeQBVCuaYrBf4kIW5rQgSthZet-ak7AcFiiujQFStyVkapF8m1J8-wVyx076mMrN3tprpWUgjLA8zP_RH3RIBl8V_bTJnPGD8t2ihN2huySpw4p6vRAUXrPqNolMsbItRZr1jBLRSKc7-3G3pxbbUCWgK0Q5uWaR45F0Lwsq0Ok-eybqeaXpc1CqGMyh-gh-8eaVGPWVaSafYfakTR8IDiY4LCFGzO2j0edh95n5uCN1Gh4okL_BW5qA_b3F08ooo6-33l3tAxKqiog0KGBzLUXXnyaC2zVVmOBNKVHPomCddIpXY35sInW0h_yvWnO-gYXS9gaUOHvPKpmWwsayExoxXJOhZ7uG8d9wzTehGTxouRIJFz5KZlx5-JLYDp-npXLNCD2hu_lG2h_5ziAFxL4RN9WmOOyi-3AzxxDmJmg6G4gejd3zSBSGDy3PgwJBnHXWcqHGrGI45hAFXlMkO4ub31mku60JxRLaJiRW9s6aD0ENkOk5dJiunkKP-OBxSElVLQtTXqMln89040lCzysMABM3jvKSz960C9im2xzzHPaIWP6TA62orRwbTy2N-wwOE9r9l_fpbUNyfpAlyxH_kABjkf8oML1l4pl7JdfdjwNry0xE_rI2ZksfZFKX1n528DPA6D1UIyfeuMoaWZuygOJGwmrUk9alePz4nj_fgWDpc3XrI4hAXgGRvNE7EJxMj8Gk4Hd_mGhIe-tSSGgzJxFlszItg9aSAr_LYqMPjPcvr6l9Xb45XJh5_FvGKmkOUGkMRssFrKKqZIFxfQohd0MDbPIKZDOzPiNepbU5tpVgeYMCkjTSJYbTo0dYiS9OrE1Z6zbIX1CXzxExQCrckTKzYGuOru9vRQO5SA9xZVV3pgZih72_ud93mmb8WTpjeFz1p4hgeU1a6TRJ8Xrnjfp2msKiUJzo2V4cM5lTf86qHNoYXJkX2lkzg07ZCmicGQA.pwNefcOHvJ45nmV71cAM3dYgQKpu3UhfSjkoE5NYNNs', 'h-captcha-response': 'P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hKdwYXNza2V5xQQjhox84v_tK8EPiufmBlxYH_KvXi9z2FBNmsAlXBt_JvFK-BsGWrzybBJS-mL1BvL63eaLkvQ-914hJJZ8hjGHH8M3idwPVGnkZROvSOoimFNAp9C0Ru8YE0Fb5MPMErECLCYBxLsX0Up4YVVcFH6TG_EetGYF4FUQF6LBhjWWZgqP3qjy0RFNcgTQ9S57yQZHjjuZwD4c-i0rhzBHnwjKbVW6KgYcKPNWXs5B7g8cNoYDKOXq3wUcbyxDV3hUXPwj3rojNK-oxxeV4p6hBWDqCAJEdFERORAYNoDtds4EtOOfDWb-ZhWDPs5KPXWje9-yupREMGrII4h4p-Wp4veb3Pa9mNHR08Qkxh1WivfGs97eOgdkO74nKCGSyIU4CMVxWuKB9nUfXQH2jFjhB2lszG9k9O8VcWldRyjD6h09HPYOClQRO3pW_EcQLtp8R-OGR7sM6S4jTcUh2ehdU-LMbTYjo_Q5nVxporeQBVCuaYrBf4kIW5rQgSthZet-ak7AcFiiujQFStyVkapF8m1J8-wVyx076mMrN3tprpWUgjLA8zP_RH3RIBl8V_bTJnPGD8t2ihN2huySpw4p6vRAUXrPqNolMsbItRZr1jBLRSKc7-3G3pxbbUCWgK0Q5uWaR45F0Lwsq0Ok-eybqeaXpc1CqGMyh-gh-8eaVGPWVaSafYfakTR8IDiY4LCFGzO2j0edh95n5uCN1Gh4okL_BW5qA_b3F08ooo6-33l3tAxKqiog0KGBzLUXXnyaC2zVVmOBNKVHPomCddIpXY35sInW0h_yvWnO-gYXS9gaUOHvPKpmWwsayExoxXJOhZ7uG8d9wzTehGTxouRIJFz5KZlx5-JLYDp-npXLNCD2hu_lG2h_5ziAFxL4RN9WmOOyi-3AzxxDmJmg6G4gejd3zSBSGDy3PgwJBnHXWcqHGrGI45hAFXlMkO4ub31mku60JxRLaJiRW9s6aD0ENkOk5dJiunkKP-OBxSElVLQtTXqMln89040lCzysMABM3jvKSz960C9im2xzzHPaIWP6TA62orRwbTy2N-wwOE9r9l_fpbUNyfpAlyxH_kABjkf8oML1l4pl7JdfdjwNry0xE_rI2ZksfZFKX1n528DPA6D1UIyfeuMoaWZuygOJGwmrUk9alePz4nj_fgWDpc3XrI4hAXgGRvNE7EJxMj8Gk4Hd_mGhIe-tSSGgzJxFlszItg9aSAr_LYqMPjPcvr6l9Xb45XJh5_FvGKmkOUGkMRssFrKKqZIFxfQohd0MDbPIKZDOzPiNepbU5tpVgeYMCkjTSJYbTo0dYiS9OrE1Z6zbIX1CXzxExQCrckTKzYGuOru9vRQO5SA9xZVV3pgZih72_ud93mmb8WTpjeFz1p4hgeU1a6TRJ8Xrnjfp2msKiUJzo2V4cM5lTf86qHNoYXJkX2lkzg07ZCmicGQA.pwNefcOHvJ45nmV71cAM3dYgQKpu3UhfSjkoE5NYNNs'}
response_2 = requests.post('https://www.file-upload.org/gy4xwjd0ec4h', data=post_data_2)

random_sleep()

element_id = 'download-btn'
element = driver.find_element(By.ID, element_id)

file_url = element.get_attribute('href')
file_response = requests.get(file_url)
with open('downloaded_file.zip', 'wb') as file:
    file.write(file_response.content)

# Delete the downloaded file
os.remove('downloaded_file.zip')

driver.quit()
