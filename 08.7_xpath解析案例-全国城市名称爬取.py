#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
#需求：解析出所有城市名称https://www.aqistudy.cn/historydata/
# if __name__ == '__main__':
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'
#     }
#     url = 'https://www.aqistudy.cn/historydata/'
#     page_text = requests.get(url=url,headers=headers).text
#
#     tree = etree.HTML(page_text)
#     hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
#     all_city_names = []
#     for li in hot_li_list:
#         hot_city_name = li.xpath('./a/text()')[0]
#         all_city_names.append(hot_city_name)
#     # print(all_city_names)
#
#     #解析的是全部城市的名称
#     # all_li_list = tree.xpath('//div[@class="all"]/div[2]/ul/div[2]/li')
#     all_li_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
#     for li in all_li_list:
#         all_city = li.xpath('./a/text()')[0]
#         all_city_names.append(all_city)
#
#     print(all_city_names,len(all_city_names))

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url,headers=headers).text

    tree = etree.HTML(page_text)
    #解析到热门城市和所有城市对应的a标签
    # //div[@class="bottom"]/ul/li/a 热门城市a标签的层级关系
    # //div[@class="bottom"]/ul/div[2]/li/a 全部城市a标签的层级关系
    # | 表达“或”的连接符
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names = []
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)
    print(all_city_names,len(all_city_names))