from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
load_dotenv()

options = Options()
options.set_preference("permissions.default.microphone",1)
options.set_preference("permissions.default.camera",1)

browser = webdriver.Chrome(executable_path=f"{os.getcwd()}/web_driver/geckodriver.exe", options=options)
browser.get('https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fwww.google.com%2F&_ga=2.155881595.1533375318.1653442791-696588692.1653442791&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

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

sleep(2)