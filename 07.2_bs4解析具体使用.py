#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
if __name__ == '__main__':
    #将本地的html文档中的数据加载到该对象中
    fp = open('./test.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    # print(soup)
    # print(soup.script) #soup.tagName 返回的是html中第一次出现的tagName标签
    # print(soup.div)
    #find('tagName'):等同于soup.div
    # print(soup.find('div')) #print(soup.div)
    #soup.find('div',class_/id/attr='chart-container')
    # print(soup.find('div',class_='head').get_text()) #class_为参数名称，class为关键字
    # print(soup.find_all('script')) #soup.find_all('tagName'): 返回符合要求的所有标签（列表）
    # print(soup.select('.menu > a')[0]) #层级选择器的使用：>表示一个层级；空格表示多个层级
    # print(soup.select('.menu > a')[0].get_text())  #soup.a.text/string/get_text()： 获取标签之间的文本数据
    # text/get_text():可以获取某一个标签中所有的文本内容；string： 只可以获取该标签下面直系的文本内容
    print(soup.select('.menu > a')[0]['href'])  #soup.a['href']获取标签中的属性值
