import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://appbrewery.github.io/Zillow-Clone/"
content = requests.get(URL).text

soup = BeautifulSoup(content, "html.parser")

elements = soup.select(".StyledPropertyCardDataWrapper")

anchor = [ele.select_one("a").get("href") for ele in elements]
address = [ele.select_one("address").text.replace("|", " ").strip() for ele in elements]
price = [ele.select_one(".PropertyCardWrapper span").text.replace("+", "/").split("/")[0] for ele in elements]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

for i in range(len(anchor)):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://forms.gle/vpL6pV1hMxSMRZA76")

    time.sleep(2)

    addressEle = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div['
                                     '1]/input')
    priceEle = driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div['
                                   '1]/input')
    linkEle = driver.find_element(By.XPATH,
                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div['
                                  '1]/input')
    submitButton = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    addressEle.send_keys(address[i])
    priceEle.send_keys(price[i])
    linkEle.send_keys(anchor[i])

    time.sleep(1)

    submitButton.click()

    driver.quit()
