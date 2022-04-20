from selenium import webdriver
import json
from selenium.webdriver.common.by import By
import time  # we might need to insert some delay in the code
from selenium.webdriver.chrome.service import Service

# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#
# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome()
driver = webdriver.Chrome()  # set path to chromedriver if you have no PATH
# driver.get("https://www.tvnet.lv/")
url = "https://www.ss.com/"
driver.get(url)  # this will open the url in browser
time.sleep(2)  # this will wait for 2 seconds
vieglie_auto = driver.find_element(by=By.ID, value="mtd_97")
#driver.find_element(by=BY.ID, value="mtd_59") .click()
# this id is for this particular page
print(vieglie_auto.text)
#print(vieglie_auto.get_attribute("href"))
#print(vieglie_auto.get_attribute("nosuchattributehref"))
vieglie_auto.click()
time.sleep(0.5)
bmw_auto = driver.find_element(by=By.LINK_TEXT, value="BMW")  # there is also a singular  find_element which find first match
print(bmw_auto.text)
bmw_auto.click()
time.sleep(1)
car_list=tuple()
car_num=0

for car in driver.find_elements(by=By.CLASS_NAME, value="am"):
    car_attrs = []
    car_num+=1
    # print(car.text)
    # print(car.get_attribute("href"))
    search_value="tr_"+car.get_attribute("id")[3:]
    # print(search_value)
    # print(car_id)
    # print(car_id[3:])
    car_attrs=[str(car_num)+","+car.text+","+car.get_attribute("href")]
    attrs = driver.find_element(by=By.ID, value=search_value)
    attrs.find_elements(by=By.CLASS_NAME,value="amopt")
        # // *[ @ id = "tr_50976088"] / td[7]
    attrs_text=attrs.text.split(",")
    # print(attrs_text)
    car_attrs.append(attrs_text)
    car_list=car_list+tuple([car_attrs])

print(car_list)
file_name="data_file_bmw_cars.json"
with open(file_name, mode="w",encoding="utf-8") as write_file:
    json.dump(car_list, write_file, indent=4, ensure_ascii=False)
print('Data has been written to file ', file_name)
