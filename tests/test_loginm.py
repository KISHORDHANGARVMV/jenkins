from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set Chrome options
options = Options()

# Disable headless mode to see the browser window
# Remove the comment below if you want to run it in non-headless mode:
# options.add_argument("--headless")  # Leave this commented or remove for visible browser

# Additional arguments to fix issues on CI servers (like Jenkins)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Set up ChromeDriver (automatically installs the correct version of ChromeDriver)
service = Service(ChromeDriverManager().install())

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open Google
driver.get("https://www.google.com")

# Wait a few seconds so you can see the browser window (optional)
import time
time.sleep(5)  # You can adjust this time

# Close the browser after the test (optional)
driver.quit()
