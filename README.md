# Web_Brute_Force_Login

Title: Web Automation for Password Testing using Selenium

Abstract:

This project introduces a web automation approach for password testing using the Selenium framework. The developed script is a versatile tool that can be applied to assess the security of login systems on websites. The script automates the process of attempting login with various password combinations, allowing users to evaluate the strength of their passwords and detect vulnerabilities in web-based authentication systems.

1. Introduction:

Security testing is a fundamental practice to ensure the robustness of web-based authentication systems. Commonly, security analysts and penetration testers use automated tools to evaluate password strength, identify weak passwords, and potentially uncover security flaws. This project aims to facilitate this process by introducing a Python script that employs the Selenium framework for web automation. The script systematically generates and tests passwords, providing valuable insights into the security of online login systems.

2. Script Components:

The script consists of several key components:

    Initialize Driver (initialize_driver(URL))

    This function initializes a headless Chrome WebDriver. Users can specify the target URL of the login page.

    Find Email Field (find_email_field(driver))

    This function locates the email or username input field on the login page using its CSS selector.

    Find Password Field (find_password_field(driver))

    This function finds the password input field using its CSS selector. It employs WebDriverWait to ensure that the field is clickable.

    Find Submit Button (find_submit_button(driver))

    Similar to the password field, this function identifies the submit button by its CSS selector and waits for it to become clickable.

    Comparing Strings (compare_strings(str1, str2))

    A utility function that compares two strings and determines their relationship, aiding in sorting and selecting passwords.

    **Password Attack (attack(URL, email_value, root, first_password, character_set, length))

    The core function of the script, which performs the password testing. It systematically generates different password combinations and tests them. The function is designed to restart the WebDriver after a specified number of attempts to prevent potential blocking by the target website.

3. How to Use the Script:

To adapt this script for your specific purposes, follow these guidelines:

    URL (URL): Replace this variable with the URL of the login page you want to test.

    Email or Username (email_value): Set the email_value variable to the email or username you wish to use for testing.

    Password Base (root): Define a common base for the passwords you want to test. This base remains constant for all generated passwords.

    First Password (first_password): Specify the initial password from which testing will begin.

    Character Set (character_set): Modify this variable to define the character set from which passwords will be generated. By default, it includes only digits (0-9), but you can expand it to include uppercase and lowercase letters and special characters according to your requirements.

    Password Length (length): Define the maximum length for the passwords you want to test.

By customizing these variables, users can utilize the script to assess the security of various online login systems, making it a valuable tool for both security professionals and developers.

4. Conclusion:

The web automation script presented in this project offers a systematic approach to password testing, enabling users to evaluate the security of online login systems. By following the provided guidelines and adapting the script for specific projects, users can uncover vulnerabilities, detect weak passwords, and contribute to enhancing the security of web-based applications.

This script empowers security professionals and developers to proactively address security issues in web applications, ultimately leading to safer and more robust online systems.
