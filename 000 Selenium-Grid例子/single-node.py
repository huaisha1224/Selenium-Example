#!/usr/bin/env python3
#encoding = utf-8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 指定Hub服务器地址、并设定浏览器
driver = webdriver.Remote(
     command_executor='http://192.168.104.209:4444/wd/hub',
     desired_capabilities=DesiredCapabilities.FIREFOX)

# 访问百度、并执行搜索操作
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()
driver.close()
