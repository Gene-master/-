#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
#需求：爬取发改委通知公告
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    #爬取页面源码数据
    url = 'https://www.ndrc.gov.cn/xwdt/tzgg/?code=&state=123'
    page = requests.get(url=url,headers=headers)
    page.encoding ='utf-8'
    page_text = page.text
    # print(page_text)

    #数据解析
    tree = etree.HTML(page_text)
    #存储的就是li标签对象
    li_list = tree.xpath('//ul[@class="u-list"]/li')
    fp = open('./FGWTZGG.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.xpath('./a/text()')
        if len(title) == 0:
            detail_url = "none"
        else:
            detail_url = 'https://www.ndrc.gov.cn/xwdt/tzgg/'+li.xpath('./a/@href')[0]
        # print(detail_url)
            detail_page = requests.get(url=detail_url, headers=headers)
            detail_page.encoding = 'utf-8'
            detail_page_text = detail_page.text
            tree = etree.HTML(detail_page_text)
            doc_h_url = tree.xpath('//div[@class="attachment_r"]/p/a/@href')
            # print(doc_h_url)
            if len(doc_h_url) == 0:
                doc_h_url = "none"
            else:
                doc_h_url_t = tree.xpath('//div[@class="attachment_r"]/p/a/@href')[0]
                doc_url = detail_url+doc_h_url_t
                # print(doc_url)
                title_text = li.xpath('./a/text()')[0]
                fp.write(title_text + ':' + doc_url + '\n')
                print(title, '爬取成功！！！')