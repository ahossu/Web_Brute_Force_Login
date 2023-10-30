# Web Automation for Password Testing using Selenium

This project introduces a web automation approach for password testing using the Selenium framework. The developed script is a versatile tool that can be applied to assess the security of login systems on websites. The script automates the process of attempting login with various password combinations, allowing users to evaluate the strength of their passwords and detect vulnerabilities in web-based authentication systems.

This is a software that is used to crack passwords using brufe-forece method. Please use it in accordance with the website's policy.

## Table of Contents

- [Introduction](#introduction)
- [Script Overview](#script-overview)
- [Configuration](#configuration)
- [Conclusion](#conclusion)

#### Link for passwords list: [full_password_list.txt](https://drive.google.com/file/d/1rzYWUeJiCynnA9pYlR9m9rtKehCLAt2q/view?usp=drivesdk "Google Drive")

## Introduction

Security testing is a fundamental practice to ensure the robustness of web-based authentication systems. Commonly, security analysts and penetration testers use automated tools to evaluate password strength, identify weak passwords, and potentially uncover security flaws. This project aims to facilitate this process by introducing a Python script that employs the Selenium framework for web automation. The script systematically generates and tests passwords, providing valuable insights into the security of online login systems.

## Script Overview

The script consists of several key components:

- **Initialize Driver (initialize_driver(URL))**

  This function initializes a headless Chrome WebDriver. Users can specify the target URL of the login page.

- **Find Email Field (find_email_field(driver))**

  This function locates the email or username input field on the login page using its CSS selector.

- **Find Password Field (find_password_field(driver))**

  This function finds the password input field using its CSS selector. It employs WebDriverWait to ensure that the field is clickable.

- **Find Submit Button (find_submit_button(driver))**

  Similar to the password field, this function identifies the submit button by its CSS selector and waits for it to become clickable.

- **Password Attack (attack(URL, email_value, password_file))**

  The core function of the script, which performs the password testing. It systematically generates different password combinations and tests them. The function is designed to restart the WebDriver after a specified number of attempts to prevent potential blocking by the target website.

## Configuration

To adapt this script for your specific purposes, follow these guidelines:

- **URL (URL):** Replace this variable with the URL of the login page you want to test.

- **Email or Username (email_value):** Set the email_value variable to the email or username you wish to use for testing.

By customizing these variables, users can utilize the script to assess the security of various online login systems, making it a valuable tool for both security professionals and developers.

#### Example of usage
``` python
if __name__ == "__main__":
    url = 'https://example.com/login'
    email = 'Username'
    password_list_file = 'full_password_list.txt'
    attack(url, email, password_list_file)
```

## Conclusion

The web automation script presented in this project offers a systematic approach to password testing, enabling users to evaluate the security of online login systems. By following the provided guidelines and adapting the script for specific projects, users can uncover vulnerabilities, detect weak passwords, and contribute to enhancing the security of web-based applications.

This script empowers security professionals and developers to proactively address security issues in web applications, ultimately leading to safer and more robust online systems.
