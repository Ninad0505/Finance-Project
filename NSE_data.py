from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

f = open('Companies_List.txt', 'r')
for word in f:


    driver = webdriver.Chrome(r"C:\Users\ninad_10a9fsk\webdriver\chromedriver.exe")
    driver.maximize_window() #For maximizing window
    driver.implicitly_wait(20) #gives an implicit wait for 20 seconds

    driver.set_page_load_timeout(10)
    driver.get(r'https://www.nseindia.com/products/content/equities/equities/eq_security.htm')
    driver.find_element_by_name('symbol').send_keys(word)
    obj = Select(driver.find_element_by_name('dateRange'))
    obj.select_by_index(5)
    driver.find_element_by_class_name('getdata-button').click()
    driver.find_element_by_class_name('download-data-link').click()

    time.sleep(4)
    driver.quit()


