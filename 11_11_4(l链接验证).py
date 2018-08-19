# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 10:12:29 2018

参考网址：https://www.jianshu.com/p/5abf51cf3211

11/11/4： 链接验证

@author: NEVERGUVEIP
"""

import bs4, requests
# todo: use beautifulsoup4 to seek out all <a> in url page ; (or use webdriver)
url = 'https://blog.csdn.net/'
res = requests.get(url)
res.raise_for_status()
res_soup = bs4.BeautifulSoup(res.text,'lxml')
res_soup_a = res_soup.select('a[href]')
print('There are %d <a href=""> in %s' % (len(res_soup_a), url))

# todo: use requests to test the href in <a>; (or use webdriver.find_element)
for i in range(len(res_soup_a)):
    a_href_url = res_soup_a[i].get('href')
    if a_href_url.startswith("http:") or a_href_url.startswith('https:'):
        a_href_url_fullname = a_href_url
    else:
        a_href_url_fullname = 'https://blog.csdn.net/' + a_href_url.replace('/new/','')
    try:
        a_res = requests.get(a_href_url_fullname, timeout=0.1)
# if status_code == 404, write the url and tag_text in txt
        if a_res.status_code == 404:
            print('This url(%s) link to 404 not found... \n %s' % (res_soup_a[i].getText(),a_href_url))
    except requests.exceptions.Timeout:
        print('A url request over time...')

print('Done!')

