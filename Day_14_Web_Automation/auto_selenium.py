from selenium import webdriver
import time  # we might need to insert some delay in the code
from selenium.webdriver.chrome.service import Service

# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
#
# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome()
driver = webdriver.Chrome("C:\\Temp\\chromedriver.exe")  # set path to chromedriver if you have no PATH
# driver.get("https://www.tvnet.lv/")
url = "https://www.ss.com/"
driver.get(url)  # this will open the url in browser
time.sleep(2)  # this will wait for 2 seconds
apartment_element = driver.find_element_by_id("mtd_59")  # this id is for this particular page
# print(apartment_element.attributes)
print(apartment_element.get_attribute("href"))
print(apartment_element.get_attribute("nosuchattributehref"))
apartment_element.click()
time.sleep(0.5)
regions = driver.find_elements_by_tag_name("h4")  # there is also a singular  find_element which find first match
print("Found", len(regions), "regions")
first_region = regions[0]  # should be Riga in our example

# first_region_children = first_region.children  # this will return a list of elements that are children of first region
first_region

# this will return first anchor among children
first_anchor_among_children = first_region_children.find_element_by_tag_name("a")
print(first_anchor_among_children.get_attribute("href"))
