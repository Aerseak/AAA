import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.suning.com")

#搜索
driver.find_element_by_id("searchKeywords").send_keys("索尼")
driver.find_element_by_id("searchSubmit").click()
#点击
driver.find_element_by_name("ssdsn_search_pro_name05-1_0_0_11377629469_0000000000").click()
#跳转第二窗口
a = driver.window_handles
driver.switch_to.window(a[1])
#点击
driver.find_element_by_id("addCart").click()

# driver.find_elements_by_name("cart1_go").click()
# driver.switch_to.alert.accept()
driver.find_element_by_name("cart1_go").click()

driver.find_element_by_name("icart1_ope_buy01").click()

time.sleep(10)
driver.quit()





