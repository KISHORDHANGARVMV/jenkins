from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # Import Service class
from webdriver_manager.chrome import ChromeDriverManager  # Optional, for auto-download of ChromeDriver
import time

# Configure Chrome options for headless mode
options = Options()
options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
options.add_argument('--no-sandbox')  # Disable sandbox (important for CI/CD environments)
options.add_argument('--disable-dev-shm-usage')  # Helps with resource limitations in CI/CD
options.add_argument('--remote-debugging-port=9222')  # Allow debugging
options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
options.add_argument('--window-size=1920x1080')  # Set window size (important for headless)

# Use the Service class to specify the chromedriver path
service = Service(executable_path='/usr/bin/chromedriver')  # Update with your chromedriver path

# Initialize the WebDriver with the Service and options
driver = webdriver.Chrome(service=service, options=options)

# Navigate to Google's homepage
driver.get('https://www.google.com/')

# Wait for the page to load (optional)
time.sleep(2)

# Verify the title of the page
assert "Google" in driver.title, f"Test failed! Expected 'Google' in title, but found {driver.title}"

print("Test passed: Google homepage opened successfully!")

# Quit the browser
driver.quit()
