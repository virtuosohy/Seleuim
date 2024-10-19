import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("python")
time.sleep(3)


driver.quit()
