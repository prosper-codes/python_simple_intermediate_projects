from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Exc
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

wait = WebDriverWait(driver, 10)

# ---- LOGIN ----
driver.get("https://practicetestautomation.com/practice-test-login/")

wait.until(Exc.visibility_of_element_located((By.ID, 'username'))).send_keys('student')
wait.until(Exc.visibility_of_element_located((By.ID, 'password'))).send_keys('Password123')
wait.until(Exc.element_to_be_clickable((By.ID, 'submit'))).click()




wait.until(Exc.visibility_of_element_located((By.TAG_NAME, "h1")))

# go to contact page
driver.get("https://practicetestautomation.com/contact/")

# fill contact form
wait.until(Exc.visibility_of_element_located(
    (By.ID, "wpforms-161-field_0"))
).send_keys("John Doe")

wait.until(Exc.visibility_of_element_located(
    (By.ID, "wpforms-161-field_0-last"))
).send_keys("Doe")

wait.until(Exc.visibility_of_element_located(
    (By.ID, "wpforms-161-field_1"))
).send_keys("john@example.com")

wait.until(Exc.visibility_of_element_located(
    (By.ID, "wpforms-161-field_2"))
).send_keys("This is a Selenium automation test.")

# wait.until(Exc.element_to_be_clickable(
#     (By.ID, "wpforms-submit-161"))
# ).click()

input("Press Enter to quit")
driver.quit()