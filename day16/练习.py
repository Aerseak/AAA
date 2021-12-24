import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.gome.com.cn")

m = driver.find_element_by_xpath("//*[@id='lisnav']/li[3]/h3")
ActionChains(driver).move_to_element(m).perform()

time.sleep(5)
driver.find_element_by_partial_link_text("游戏本").click()


time.sleep(10)
driver.quit()
