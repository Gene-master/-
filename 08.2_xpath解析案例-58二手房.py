#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
#需求：爬取58二手房中的房源信息
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    #爬取页面源码数据
    url = 'https://bj.58.com/ershoufang/'
    page_text = requests.get(url=url,headers=headers).text
    # print(page_text)

    #数据解析
    tree = etree.HTML(page_text)
    #存储的就是section标签对象
    div_list = tree.xpath('//section[@class="list"]/div')
    for div in div_list:
        title = div.xpath('./a/div[2]/div/div/h3/text()')[0]
        print(title)