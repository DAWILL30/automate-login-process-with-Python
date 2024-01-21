from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    # Create the driver
    driver = webdriver.Chrome(options=options)
    # Connect to the current webpage
    driver.get('http://automated.pythonanywhere.com/login/')
    return driver

def main():
    driver = get_driver()

    # Find and fill the username and wait for it to be present
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'id_username'))
    )
    username_input.send_keys('automated')

    # Find and fill the password and wait for it to be present
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'id_password'))
    )
    password_input.send_keys('automatedautomated' + Keys.RETURN)

    # Click the home link and wait for it to be clickable
    home_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/nav/div/a'))
    )
    home_link.click()

    # Print the current URL in the terminal
    print(driver.current_url)

if __name__ == '__main__':
    main()

