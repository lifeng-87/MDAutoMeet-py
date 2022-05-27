from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from dotenv import load_dotenv
import os
load_dotenv()

options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-infobars")
options.add_experimental_option("detach", True)
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
})

browser = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()), options=options)
browser.get('https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

WebDriverWait(browser, 2000).until(
    EC.presence_of_element_located((By.ID, "identifierId"))
)

account = browser.find_element(By.ID, "identifierId")
account.send_keys(os.getenv("ACCOUNT"))

next = browser.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
next.click()

WebDriverWait(browser, 2000).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
)

passwd = browser.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
passwd.send_keys(os.getenv("PASSWD"))

next = browser.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
next.click()