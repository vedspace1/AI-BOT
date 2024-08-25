from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

 #Initialize the WebDriver
chrome_options = Options()

# Set up the service
service = Service(r"C:\Users\Welcome\Downloads\bot_linkedin\chromedriver-win64\chromedriver.exe")

# Initialize the WebDriver with Options and Service
driver = webdriver.Chrome(service=service, options=chrome_options)

print("Browser opened successfully")

# Open LinkedIn and log in
driver.get("https://www.linkedin.com/login")
time.sleep(2)

# Enter username and password
username = driver.find_element(By.ID, "username")
username.send_keys("oksomeone009@gmail.com")

password = driver.find_element(By.ID, "password")
password.send_keys("OksomeoneBye")

# Click on the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(5)  # Adjust this time if needed

# Navigate to connections page
driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
time.sleep(5)

# Define your message template
message_template = "Hi [Name], Good to connect with you. How're you doing? Just want to say Hi!"
def send_dm_to_connection():
    while True:
        # Find all connection elements with "Message" buttons on the current page
        message_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Message')]")


        for index, message_button in enumerate(message_buttons):
            try:
                # Click on the message button to open the DM window
                message_button.click()
                time.sleep(2)  # Wait for the DM window to open

                # Find the DM text area
                dm_textarea = driver.find_element(By.XPATH, "//div[@role='textbox']")

                # Get the connection's name (optional)
                connection_name = driver.find_element(By.XPATH, "//h2[contains(@class,'msg-entity__name')]").text
                
                # Customize the message with the connection's name
                personalized_message = message_template.replace("[Name]", connection_name)

                # Send the message
                dm_textarea.send_keys(personalized_message)
                time.sleep(1)  # Wait before sending
                dm_textarea.send_keys(Keys.RETURN)
                time.sleep(2)  # Wait after sending

                print(f"Sent message to {connection_name}")

                # Close the DM window to go back to the connections page
                close_button = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
                close_button.click()
                time.sleep(2)  # Wait for the page to return to normal state
            except Exception as e:
                print(f"Failed to send message to a connection: {e}")
                continue

        # After processing all buttons on the page, move to the next page of connections
        try:
            next_button = driver.find_element(By.XPATH, "//button[@aria-label='Next']")
            next_button.click()
            time.sleep(3)  # Wait for the next page to load
        except Exception as e:
            print(f"Couldn't find the next page button: {e}")
            break  # Stop if there's no next page

# Run the function
send_dm_to_connection()
