from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set Chrome options
options = Options()

# Don't use headless mode to see the browser window
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Set up ChromeDriver (automatically installs the correct version of ChromeDriver)
service = Service(ChromeDriverManager().install())

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open the URL
driver.get("https://www.google.com")

# Wait for a few seconds to see the page (Optional)
import time
time.sleep(5)  # You can increase this time if needed

# Close the browser after the test (optional)
driver.quit()
