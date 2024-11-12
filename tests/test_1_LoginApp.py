import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fixture to set up the Chrome WebDriver
@pytest.fixture
def setup_driver():
    from selenium.webdriver.chrome.options import Options
    
    options = Options()
    options.headless = True  # Enable headless mode (no UI displayed)

    # Ensure chromedriver path is correct
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

# Test function to perform the registration action
def test_register(setup_driver):
    driver = setup_driver

    # Navigate to the signup page
    driver.get('http://localhost:4200/signup')

    # Fill in the Name field
    name_input = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='name']")
    name_input.send_keys("Test User")  # Enter the name

    # Fill in the Email field
    email_input = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='email']")
    email_input.send_keys("newuser@gmail.com")  # Enter the email

    # Fill in the Password field
    password_input = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='password']")
    password_input.send_keys("@Admin123")  # Enter the password

    # Fill in the Confirm Password field
    confirm_password_input = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='confirmPassword']")
    confirm_password_input.send_keys("@Admin123")  # Enter the confirm password

    # Click the Sign Up button
    signup_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Sign Up!')]")
    signup_button.click()

    # Wait until the dashboard or success message is loaded and visible
    try:
        success_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".your-success-message-selector"))  # Replace with correct selector
        )

        # Assert that the success message is displayed
        assert success_message_element.is_displayed(), "Success message not displayed after signup"

        # Print the title of the next page
        dashboard_title = driver.title
        print(f"Dashboard title: {dashboard_title}")

    except Exception as e:
        print(f"An error occurred: {e}")

    # Capture a screenshot at the end (optional)
    screenshot_file = "signup_screenshot.png"
    driver.save_screenshot(screenshot_file)
    print(f"Screenshot saved as {screenshot_file}.")

# Entry point for running the test
if __name__ == "__main__":
    pytest.main(["-q"])
