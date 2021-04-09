# Google arama sonucunda gelen sitelerin Taglarını, linklerini ve descriptionlarını kaydeden program
# https://www.youtube.com/watch?v=ztbFY_kL4jI
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=hasan")
#assert "Python" in driver.title
time.sleep(1)
for element in driver.find_elements_by_xpath('//div[@id="search"]//div[@class="g"]'): # Burada id'si search olan divin içindeki class'ı g olan divi aradık
    # Ana dizin yukardaki. Aşağıdakileri bu ana dizinin içinde aradığımız için . ile başladık.
    title = element.find_element_by_xpath('.//h3[@class="LC20lb DKV0Md"]').text
    link = element.find_element_by_xpath('.//div[@class="yuRUbf"]/a').get_attribute('href') # burada classı yurubf olan divin içindeki a daki href i aradık. fotosunu atıyorum.
    description = element.find_element_by_xpath('.//span[@class="aCOpRe"]').text
    #detail = element.find_element_by_xpath('.//span[@class="aCOpRe"]').text
    print(title)
    print(link)
    print(description)
    print("--------------------------------------------")
