#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os
import re
#需求：爬取网页中所有免费简历模板并下载 https://aspx.sc.chinaz.com/query.aspx?keyword=%E5%85%8D%E8%B4%B9&classID=864

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url = 'https://aspx.sc.chinaz.com/query.aspx?keyword=%E5%85%8D%E8%B4%B9&issale=&classID=864&page=1' # 由于页码构成为page=%d，不能用原new_url = format（url % pageNum）进行页面循环

    # 创建一个文件夹，保存所有的文件
    if not os.path.exists('./jianli_muban'):
        os.mkdir('./jianli_muban')

    # 多页面“浏览”
    for i in range(1,3):
        # 对应页码的url
        # new_url = url.format(pageNum)
        new_url = re.sub('page=\d+', 'page=%d' %i, url, re.S)  #适用于page=%d的页面循环方式，range可以调试（※再学习）
        # print(new_url)


        # 获取页面信息
        page_text = requests.get(url=new_url,headers=headers).text
        # print(page_text)
        tree = etree.HTML(page_text)

        # 解析每一页各个免费模板的预览链接
        div_list = tree.xpath('//div[@class="main_list jl_main"]/div')

        # 建立记录小本本
        fp = open('./JLMB.txt', 'w', encoding='utf-8')
        # all_table_url = []

        # 循环div爬取地址
        for div in div_list:
            table_url = 'https:'+div.xpath('./a/@href')[0]
            title = div.xpath('./a/img/@alt')[0]
            # print(title)
            # all_table_url.append(table_url)
            # all_url = ''.join(all_table_url)
            # print(all_table_url,len(all_table_url))

            page_each = requests.get(url=table_url,headers=headers)
            page_each.encoding = 'utf-8'
            page_each_text = page_each.text
            # print(page_each_text)

            page_each_text_t = etree.HTML(page_each_text)
            # //*[@id="down"]/div[2]/ul
            a_url = page_each_text_t.xpath('//div[@class="down_wrap"]/div[2]/ul/li/a/@href')[0]
            # print(a_url)

            # 小本本记好内容
            # fp.write(title + ':' + a_url + '\n')
            # print(title, '爬取成功！！！')

            # 文件夹下载好
            # 请求到了文件的二进制数据
            Muban_data = requests.get(url=a_url,headers=headers).content
            # print(Muban_data)

            # 生成文件名称
            Muban_name = title.split('/')[-1]
            # 文件存储路径
            Muban_Path = './jianli_muban/' + title+'.rar'
            with open(Muban_Path, 'wb') as fp:
                fp.write(Muban_data)
                print(Muban_name, '下载成功！！！')


