import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
driver.find_element(By.LINK_TEXT,"新闻").click()
time.sleep(3)


driver.quit()
