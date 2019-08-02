#!/usr/bin/env python3
#encoding = utf-8


from selenium import webdriver
import time
import csv
import json


def buff_pubg():
    """
    从buff.163.com获取Pubg的饰品价格
    """
    pubg_price = {}
    pubg_headers = ['name','money']
    driver = webdriver.Firefox()
    for page in range(1,15):
        url = ('https://buff.163.com/market/?game=pubg#tab=selling&page_num=%s&sort_by=price.desc' %page)
        print('第%s页:'%page,url)
        driver.get(url)
        driver.refresh()

        #判断Buff的定位规则
        try:
            is_xpath = driver.find_element_by_xpath('/html/body/div[6]/div/div[4]/div[1]/ul/li[1]/h3/a').text
            if len(is_xpath) >= 1:
                name_xpath = 6
        except:
            name_xpath = 5
            pass


        #获取饰品名称和价格
        for i in range(1,21):
            try:
                if name_xpath == 6:
                    name = driver.find_element_by_xpath(
                        ('/html/body/div[6]/div/div[4]/div[1]/ul/li[%s]/h3/a') %i)
                    money = driver.find_element_by_xpath(
                        ('/html/body/div[6]/div/div[4]/div[1]/ul/li[%s]/p/strong') %i)
                    pubg_price[name.text] = money.text[1:] #把饰品名称和对应的价格写入到字典里面

                elif name_xpath == 5:
                    name = driver.find_element_by_xpath(
                        ('/html/body/div[5]/div/div[4]/div[1]/ul/li[%s]/h3/a') %i)
                    money = driver.find_element_by_xpath(
                        ('/html/body/div[5]/div/div[4]/div[1]/ul/li[%s]/p/strong') %i)
                    pubg_price[name.text] = money.text[1:]
            except:
                pass
        #print(pubg_price)

    driver.close()

    #print(pubg_price)
    #写入内容到csv文件
    try:
        with open('buff_pubg.csv', 'a+', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=pubg_headers)
            writer.writeheader()
            for k,v in pubg_price.items():
                #print(k,v)
                writer.writerow({'name': k, 'money': v})
            csvfile.close()
    except:
        pass
#---------------------------------------------------------------------------------------------------

def buff_dota2():
    """
    从buff.163.com上获取Dota2的饰品价格
    """
    dota2_price = {}
    dota2_headers = ['name','money']
    dota2_driver = webdriver.Firefox()
    for page in range(1,327): #327
        url = ('https://buff.163.com/market/?game=dota2#tab=selling&page_num=%s&sort_by=price.desc' %page)
        print('第%s页'%page, url)
        dota2_driver.get(url)
        dota2_driver.refresh()

        #判断buff饰品定位是否准确
        try:
            is_xpath = driver.find_element_by_xpath('/html/body/div[6]/div/div[4]/div[1]/ul/li[1]/h3/a').text
            if len(is_xpath) >= 1:
                name_xpath = 6
        except:
            name_xpath = 5
            pass

        for i in range(1,21):
            #获取Dota2饰品价格
            try:
                if name_xpath == 6:
                    dota2_name = dota2_driver.find_element_by_xpath(
                        ('/html/body/div[6]/div/div[4]/div[1]/ul/li[%s]/h3/a') %i)
                    dota2_money = dota2_driver.find_element_by_xpath(
                        ('/html/body/div[6]/div/div[4]/div[1]/ul/li[%s]/p/strong') %i)
                    dota2_price[dota2_name.text] = dota2_money.text[1:]

                elif name_xpath == 5:
                    dota2_name = dota2_driver.find_element_by_xpath(
                        ('/html/body/div[5]/div/div[4]/div[1]/ul/li[%s]/h3/a') %i)
                    dota2_money = dota2_driver.find_element_by_xpath(
                        ('/html/body/div[5]/div/div[4]/div[1]/ul/li[%s]/p/strong') %i)
                    dota2_price[dota2_name.text] = dota2_money.text[1:]

            except:
                pass

    dota2_driver.close()
    #print(dota2_price)
    #把内容写入csv文件
    try:
        with open('buff_dota2.csv', 'a+', newline='') as csvdota2:
            writer = csv.DictWriter(csvdota2, fieldnames=dota2_headers)
            writer.writeheader()
            for k,v in dota2_price.items():
                #print(k,v)
                writer.writerow({'name':k, 'money':v})
            csvdota2.close()
    except:
        pass
#------------------------------------------------------------------------------------------------

def buff_csgo():
    """
    从buff.163.com上获取CSGO的饰品价格
    """
    csgo_price = {}
    csgo_headers = ['name','money']
    csgo_driver = webdriver.Firefox()

    for csgo_page in range(1,223): #CSGO饰品有222页
        url = ('https://buff.163.com/market/?game=csgo#tab=selling&page_num=%s&sort_by=price.desc' %csgo_page)
        print('第%s页'%csgo_page,url)
        csgo_driver.get(url)
        csgo_driver.refresh()

        for i in range(1,21):
            #获取CSGO饰品价格
            try:
                csgo_name = csgo_driver.find_element_by_xpath(
                    ('/html/body/div[5]/div/div[4]/div[1]/ul/li[%s]/h3/a') %i)
                csgo_money = csgo_driver.find_element_by_xpath(
                    ('/html/body/div[5]/div/div[4]/div[1]/ul/li[%s]/p/strong') %i)
                csgo_price[csgo_name.text] = csgo_money.text[1:]
            except:
                pass
    #print(csgo_price)
    # for k,v in csgo_price.items():
    #     print(k,v)

    csgo_driver.close()

    #把内容写入到json文件
    try:
        with open('buff_csgo.json','w', errors='ignore') as file:
            print(csgo_price)
            file.write(json.dumps(csgo_price, 
                #sort_keys=True, 
                indent=4, 
                ensure_ascii=False, 
                separators=(',',':')
                )
            )
    except:
        pass



if __name__ == '__main__':
    #buff_pubg()
    buff_dota2()
    #buff_csgo()


