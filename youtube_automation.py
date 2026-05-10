from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time

# Set up Edge options
edge_options = Options()
edge_options.add_argument("--start-maximized")  # Optional: start maximized

# Path to Edge WebDriver (download from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
# Selenium will automatically manage the driver if not specified
# service = Service(executable_path=r'C:\path\to\msedgedriver.exe')  # Replace with actual path

# Initialize the Edge driver
driver = webdriver.Edge(options=edge_options)

try:
    # Open YouTube
    driver.get("https://www.youtube.com")

    # Wait for the page to load
    time.sleep(2)

    # Find the search box and enter the search query
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("Hungry Cheetah Video Song")
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    time.sleep(3)

    # Click on the first video result
    first_video = driver.find_element(By.CSS_SELECTOR, "ytd-video-renderer a#video-title")
    first_video.click()

    # Wait for the video to start playing
    time.sleep(5)

    # Play for 1 minute
    time.sleep(60)

finally:
    driver.quit()