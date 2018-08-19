# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 11:28:57 2018

11.7 下载所有XKCHD漫画
XKCD是一个流行的即可漫画网站
1、加载主页
2、保存该页的漫画图片
3、转入前一章漫画链接
4、重复直到第一张漫画

a、利用request模块下载页面
b、利用Beautiful soup 找到页面中漫画图像的URL
c、利用iter_content()下载漫画图片，并保存到硬盘
d、找到前一章漫画的链接，然后重复
@author: NEVERGUVEIP
"""
#！python3
import requests,os,bs4

url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
    #download the page
    print('downloading page%s...'% url)
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text,'lxml')
    #find the url of comic image
    comicElem = soup.select('#comic img')
    if comicElem ==[]:
        print('could not find comic image')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        #download the image
        print('downloading image %s...'%(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        
        #save the image to ./xkcd
        imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(1000000):
            imageFile.write(chunk)
        imageFile.close()
    #get the prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')
        