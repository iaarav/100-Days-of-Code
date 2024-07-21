from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = ""
ACCOUNT_PASSWORD = ''

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    'https://www.linkedin.com/jobs/search/?currentJobId=3976667760&eBP=NOT_ELIGIBLE_FOR_CHARGING&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&refId=WLmud6HkfH5auKXyxcvA2A%3D%3D&trackingId=ZXyp28vl%2FcNM8HuslmLTww%3D%3D'
)

# Click Reject Cookies Button
signIn = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
signIn.click()

emailOrPhoneField = driver.find_element(By.XPATH, '//*[@id="username"]')
emailOrPhoneField.send_keys(f"{ACCOUNT_EMAIL}")

passwordField = driver.find_element(By.XPATH, '//*[@id="password"]')
passwordField.send_keys(f"{ACCOUNT_PASSWORD}")

submitButton = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
submitButton.click()

time.sleep(4)

saveButton = driver.find_element(By.CSS_SELECTOR, 'button.jobs-save-button')
saveButton.click()

driver.close()
