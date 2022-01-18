#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
#需求：爬取电影天堂【2021新品精品】电影下载链接，网址（临时链接）https://www.dytt8.net/index2.html
if __name__ == '__main__':
    #对首页的页面数据进行爬取
    headers = {
        'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 90.0.4430.212Safari / 537.36'
    }
    url = 'https://www.dytt8.net/index2.htm'
    page_content = requests.get(url=url,headers=headers).content
    # print(page_content)

    # request爬下的页面中文内容乱码，先get成bytes型，再通过str方法转换成字符型
    #page_text = str(page_content,'utf-8')

    #在首页中解析出章节的标题和详情页的url
    #1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_content,'lxml')
    #解析章节标题和详情页url
    tr_list = soup.select('.bd3 > div:nth-child(2) > div > div > div:nth-child(2) > div:nth-child(2)  tr') #header > div > div.bd2 > div.bd3 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div.co_content8 > ul > table > tbody > tr:nth-child(2) > td:nth-child(1) > a:nth-child(2)
    # print(soup.select('.bd3rl > div:nth-child(2) > div:nth-child(2)  tr'))


    fp = open('./2021xinpin_film.txt','w',encoding='utf-8')
    for tr in tr_list[1:]:
        # title = tr.a.string
        title = tr.a.next_sibling.next_sibling.string #NB了...
        # title.encode = 'utf-8'
        # print(title)

        detail_url = 'https://www.dytt8.net'+tr.a.next_sibling.next_sibling['href']
        # print(detail_url)
        #对详情页发起请求，解析出章节内容
        detail_page = requests.get(url=detail_url,headers=headers).content.decode('gbk')

        #测试：中文乱码转化（gbk）
        # detail_page = requests.get(url=detail_url, headers=headers)
        # detail_page.encoding = 'gbk'
        # detail_page_text = detail_page.text

        #测试：中文乱码转化（utf-8）
        # request爬下的页面中文内容乱码，先get成bytes型，再通过str方法转换成字符型
        # detail_page_text = str(detail_page_content,'utf-8')
        # detail_page_text = detail_page.text
        # print(detail_page)

        #测试：标准化网页代码，参考网址：https://blog.csdn.net/qq_43194257/article/details/87786316
        # detail_soup = BeautifulSoup(detail_page,'lxml')
        # print(detail_soup.prettify())

        #测试：select定位不到要素，原因参考网址：https://blog.csdn.net/zm1813695320/article/details/104466906?utm_medium=distribute.pc_feed_404.none-task-blog-2~default~BlogCommendFromBaidu~default-1.control404&depth_1-utm_source=distribute.pc_feed_404.none-task-blog-2~default~BlogCommendFromBaidu~default-1.control40
        # div_tag = detail_soup.select('.Zoom > span > a')  #Zoom > span > a
        # print(detail_soup.select('.Zoom > span > a'))

        #实践成功：正则表达
        ex = '<a target="_blank" href="magnet:(.*?)">'
        div_tag = re.findall(ex, detail_page, re.S)[0]
        # print(div_tag)
        div_mag = ''.join(div_tag) # list变str，参考网址：https://www.cnblogs.com/hwnzy/p/10927484.html
        url_download = 'magnet:'+div_mag
        # print(url_download)

        #解析到了各页面磁力链接内容
        content = url_download
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功！！！')

        #实践成功：pyinstaller -F -w 文件名.py 生成.exe