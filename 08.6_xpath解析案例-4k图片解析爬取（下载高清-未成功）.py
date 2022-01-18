#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os
#需求：解析下载图片数据 https://pic.netbian.com/4kfengjing/
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    #爬取页面图片数据
    url = 'https://pic.netbian.com/4kfengjing/'
    response = requests.get(url=url,headers=headers)
    #手动设定相应数据的编码格式
    # response.encoding ='gbk'

    response_text = response.text
    # print(page_text)

    # 数据解析：src的属性值 alt属性
    tree = etree.HTML(response_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    #创建一个文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    for li in li_list:
        img_src ='https://pic.netbian.com/'+ li.xpath('./a/@href')[0]
        img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
        #通用处理中文乱码的解决方案
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        # print(img_src,img_name)
        #请求图片进行持久化存储
        img_data = requests.get(url=img_src,headers=headers)
        #下载地址须登录，而且单日免费有限制...未成功
        img_path = 'picLibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功！！！')
