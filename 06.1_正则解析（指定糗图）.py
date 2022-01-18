#!/usr/bin/env python
# -*- coding:utf-8 -*-
#需求：爬取糗事百科中糗图板块下所有的糗图图片
import requests
if __name__ == '__main__':
    #如何爬取图片数据
    url = 'https://pic.qiushibaike.com/system/pictures/12503/125035521/small/1F3PHJFNAEZXJDM2.jpg?imageView2/1/w/150/h/112'
    #content返回的是二进制形式的图片数据
    # text（字符串） content（二进制） json（）（对象）
    img_data = requests.get(url=url).content

    with open('./qiutu.jpg','wb') as fp:
        fp.write(img_data)