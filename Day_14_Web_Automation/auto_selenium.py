from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
#
# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome()
driver = webdriver.Chrome("C:\\Temp\\chromedriver.exe")  # set path to chromedriver if you have no PATH
driver.get("https://www.tvnet.lv/")
