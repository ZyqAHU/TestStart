from selenium import webdriver

from time import sleep


driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

sleep(3)