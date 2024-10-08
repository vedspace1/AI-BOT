import openai
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Function to generate AI comments
def generate_comment(post_content):
    response = openai.ChatCompletion.create(
        model="gpt-2",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Write a thoughtful comment on the following post: {post_content}"}
        ]
    )
    return response.choices[0].message["content"].strip()
#Initialize the WebDriver
chrome_options = Options()

# Set up the service
service = Service(r"C:\Users\Welcome\Downloads\bot_linkedin\chromedriver-win64\chromedriver.exe")

# Initialize the WebDriver with Options and Service
driver = webdriver.Chrome(service=service, options=chrome_options)

print("Browser opened successfully")





# Log in to LinkedIn
driver.get("https://www.linkedin.com/login")
time.sleep(2)

username = driver.find_element(By.ID, "username")
username.send_keys("your-email")

password = driver.find_element(By.ID, "password")
password.send_keys("your-password")
password.send_keys(Keys.RETURN)

time.sleep(5)

#  Navigate to LinkedIn feed and find a post
driver.get("https://www.linkedin.com/feed/")
time.sleep(5)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

#  Extract post content (adjust selector as needed)
post_content_element = driver.find_element(By.CSS_SELECTOR, "span.break-words")
post_content = post_content_element.text

# Initialize OpenAI API key
openai.api_key = "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"



#  Generate a comment using OpenAI
comment_text = generate_comment(post_content)

#  Post the AI-generated comment
post_comment_box = driver.find_element(By.CSS_SELECTOR, "div[role='textbox']")
post_comment_box.click()
post_comment_box.send_keys(comment_text)
post_comment_box.send_keys(Keys.RETURN)

time.sleep(3)

# Step 8: Close the browser
driver.quit()


# Locate a post (adjust the selector based on LinkedIn's structure)
posts = driver.find_elements(By.XPATH, "//div[contains(@class, 'feed-shared-update-v2')]")

for post in posts:
    try:
        # Scroll to the post element
        driver.execute_script("arguments[0].scrollIntoView(true);", post)
        time.sleep(2)  # Allow time for the post to load

        # Add a comment (adjust selector based on the comment button and input field structure)
        comment_button = post.find_element(By.XPATH, ".//button[contains(@aria-label, 'comment')]")
        comment_button.click()
        time.sleep(2)

        comment_input = post.find_element(By.XPATH, ".//textarea[contains(@aria-label, 'Add a comment')]")
        comment_input.send_keys("This is a test comment generated by the bot.")

        # Submit the comment (adjust selector based on LinkedIn's structure)
        submit_button = post.find_element(By.XPATH, ".//button[contains(@aria-label, 'Post comment')]")
        submit_button.click()

        time.sleep(3)  # Wait for the comment to be posted

    except Exception as e:
        print(f"Error commenting on a post: {e}")

