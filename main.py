from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="../chromedriver.exe")
# in executable path put your chromedriver.exe path or it will not work

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=service)
driver.implicitly_wait(.5)
driver.maximize_window()

driver.get("https://www.livechat.com/typing-speed-test/#/")

while len(driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[1]").text):

    type = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[1]")
    current_word = type.text
    driver.find_element(By.CSS_SELECTOR, "#test-input").send_keys(current_word, Keys.SPACE)


