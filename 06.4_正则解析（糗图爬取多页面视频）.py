#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import os
#需求：爬取糗事百科中糗图板块下所有的糗图图片
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 90.0.4430.212Safari / 537.36'
    }
    #创建一个文件夹，保存所有的图片
    if not os.path.exists('./qiutuLibs_video'):
        os.mkdir('./qiutuLibs_video')
    #设置一个通用的url模板
    # url = 'https://www.qiushibaike.com/article/125028004'
    url = 'https://www.qiushibaike.com/video/page/%d/'
    # pageNum = 14

    for pageNum in range(1,2):
        #对应页码的url
        new_url = format(url%pageNum)

        #使用通用爬虫对url对应的一整张页面进行爬取
        page_text = requests.get(url=new_url,headers=headers).text

        #使用聚焦爬虫将页面中所有的糗图进行解析/爬取-(<img src="(.*?)" alt.*?<img src="(.*?)" alt.*?<img src="(.*?)" alt.*?)
        # ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        ex = '<source src="//q(.*?).mp4" type='
        img_src_list = re.findall(ex,page_text,re.S)
        # print(img_src_list)
        for src in img_src_list:
            #拼接出一个完整的视频url
            src = 'https://q'+src+'.mp4'
            #请求到了视频的二进制数据
            video_data = requests.get(url=src,headers=headers).content
            #生成视频名称
            video_name = src.split('/')[-1]
            #视频存储路径
            videoPath = './qiutuLibs_video/'+video_name
            with open(videoPath,'wb') as fp:
                fp.write(video_data)
                print(video_name,'下载成功！！！')


