#!/usr/bin/env python
# -*- coding:utf-8 -*-
from lxml import etree
if __name__ == '__main__':
    #实例化好了一个etree对象，且将被解析的源码加载到了该对象中
    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.parse('test.html', parser = parser)
    # r = tree.xpath('/html/body/div') # /:表示的是从根节点开始定位。表示的是一个层级。
    # r = tree.xpath('/html//div') # //：表示的是多个层级。可以表示从任意位置开始定位。
    # r = tree.xpath('//div')
    # r = tree.xpath('//div[@class="head"]') #tag[@attrName="attrValue"]
    # r = tree.xpath('//div[@class="menu-bar menu clearfix"]/a[3]')#索引从1开始不是0
    # /text():获取的是标签中直系的； # //text()：标签中非直系的文本内容（所有的文本内容）；[0]从列表变成字符串
    # r = tree.xpath('//div[@class="menu-bar menu clearfix"]//text()')
    r = tree.xpath('//div[@class ="download-code"]/img/@src') # /@attrName  ==>img/src
    print(r)
