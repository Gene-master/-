#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

if __name__ == '__main__':

    url ='http://scxk.nmpa.gov.cn:81/xk/'

    headers = {
        'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 90.0.4430.212Safari / 537.36'
    }

    page_text = requests.get(url=url,headers=headers).text
    with open('./huazhuangpin.html','w',encoding='utf-8')as fp:
        fp.write(page_text)