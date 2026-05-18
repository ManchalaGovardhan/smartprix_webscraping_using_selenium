
from selenium import webdriver
import time
import selenium.webdriver.common.keys as keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
options = Options()

# Keep browser open
options.add_experimental_option("detach", True)

# Reduce automation detection
options.add_argument("--disable-blink-features=AutomationControlled")

driver=webdriver.Chrome(options=options)
time.sleep(2)
driver.get("https://www.smartprix.com/mobiles")
time.sleep(2)
exclude_out_of_stock=driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]')
exclude_out_of_stock.click()
time.sleep(2)
exclude_upcoming=driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]')
exclude_upcoming.click()
time.sleep(2)
slim=driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[8]')
slim.click()
time.sleep(2)


old_height=driver.execute_script("return document.body.scrollHeight")


while True:
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()

    time.sleep(2)
    new_height=driver.execute_script("return document.body.scrollHeight")
    print(old_height,new_height)
    if new_height == old_height:

        break

    old_height=new_height
time.sleep(4)
html=driver.page_source
with open("mobiles.html","w",encoding="utf-8") as f:
  f.write(html)



