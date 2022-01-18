#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
#需求：爬取电影天堂中2021新品精品电影名称
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    #爬取页面源码数据
    url = 'https://www.dytt8.net/index2.htm/'
    page_text = requests.get(url=url,headers=headers).text
    print(page_text)

    # #数据解析
    # tree = etree.HTML(page_text)
    # #存储的就是div标签对象
    # tr_list = tree.xpath('//div[@class="co_content8"]/ul/table/tbody/tr')
    # for tr in tr_list:
    #     title = tr.xpath('./td/a[2]/text()')
    #     print(title)