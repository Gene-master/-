#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
#需求：爬取三国演义小说所有的章节标题和章节内容https://www.shicimingju.com/book/sanguoyanyi.html
if __name__ == '__main__':
    #对首页的页面数据进行爬取
    headers = {
        'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 90.0.4430.212Safari / 537.36'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_content = requests.get(url=url,headers=headers).content
    # request爬下的页面中文内容乱码，先get成bytes型，再通过str方法转换成字符型
    page_text = str(page_content,'utf-8')

    #在首页中解析出章节的标题和详情页的url
    #1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text,'lxml')
    #解析章节标题和详情页url
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com'+li.a['href']
        #对详情页发起请求，解析出章节内容
        detail_page_content = requests.get(url=detail_url,headers=headers).content
        # request爬下的页面中文内容乱码，先get成bytes型，再通过str方法转换成字符型
        detail_page_text = str(detail_page_content,'utf-8')
        #解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')
        #解析到了章节的内容
        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功！！！')