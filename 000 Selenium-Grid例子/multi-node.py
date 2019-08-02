#!/usr/bin/env python3
#encoding = utf-8
"""
多和Node节点、不同一个测试用例在不同的节点中运行
"""
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 添加Node节点到列表、并设定好浏览器
nodes={'http://192.168.104.172:6666/wd/hub':'chrome',
      'http://192.168.104.172:7777/wd/hub':'firefox'}

# 从列表里面取出node节点和对应的浏览器参数
for host,browser in nodes.items():
    print(host,browser)
    driver=webdriver.Remote(command_executor=host,
                            desired_capabilities={'browserName':browser})

# 访问百度、并执行搜索关键词；为了便于区分搜索关键词我们用浏览器参数
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(browser)
    driver.find_element_by_id('su').click()
    driver.close()