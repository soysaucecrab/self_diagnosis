import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

while 1:

    i = 0

    driver = webdriver.Chrome('D:\학교\자가진단\chromedriver.exe')
    url = 'https://hcs.eduro.go.kr/'
    driver.get(url)
    driver.maximize_window()
    action = ActionChains(driver)

    driver.find_element_by_id("btnConfirm2").click()
    driver.find_element_by_id("schul_name_input").click()
    time.sleep(0.2)
    driver.find_element_by_id("sidolabel").click()

    while i < 15:
        driver.find_element_by_id("sidolabel").send_keys(Keys.ARROW_DOWN)
        i = i + 1
        time.sleep(0.05)

    i = 0

    driver.find_element_by_id("crseScCode").click()
    while i < 3:
        driver.find_element_by_id("crseScCode").send_keys(Keys.ARROW_DOWN)
        i = i + 1
        time.sleep(0.05)

    driver.find_element_by_id("orgname").send_keys("압량")
    time.sleep(0.05)
    driver.find_element_by_id("sidolabel").send_keys(Keys.ENTER)
    time.sleep(0.05)
    driver.find_element_by_class_name("searchBtn").click()
    time.sleep(0.05)
    driver.find_element_by_class_name("layerSchoolArea").click()
    time.sleep(0.05)
    driver.find_element_by_class_name("layerFullBtn").click()

    driver.find_element_by_id("user_name_input").send_keys("김진우")
    driver.find_element_by_id("birthday_input").send_keys("070319")
    driver.find_element_by_id("btnConfirm").click()
    time.sleep(1)

    driver.find_element_by_class_name("keyboard-img").click()

    time.sleep(1)

    driver.find_element_by_xpath("//a[contains(@aria-label, '0')]").click()
    driver.find_element_by_xpath("//a[contains(@aria-label, '3')]").click()
    driver.find_element_by_xpath("//a[contains(@aria-label, '1')]").click()
    driver.find_element_by_xpath("//a[contains(@aria-label, '9')]").click()

    driver.find_element_by_id("btnConfirm").click()

    time.sleep(1)

    driver.find_element_by_class_name("name").click()
    time.sleep(1)
    driver.find_element_by_id("survey_q1a1").click()
    driver.find_element_by_id("survey_q2a1").click()
    driver.find_element_by_id("survey_q3a1").click()
    driver.find_element_by_id("survey_q4a1").click()

    driver.find_element_by_id("btnConfirm").click()

    time.sleep(869395)
