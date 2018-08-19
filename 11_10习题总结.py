# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 19:48:55 2018
第11章 总结和习题
@author: NEVERGUVEIP
"""
1、简单描述webbrowser、requests、BeautifulSoup、和selenium模块之间的关系
    webbrowser模块有一个open（）方法，它可以启动web浏览器，打开指定url，requests模块可以从网上下载文件和页面。
    bs4用来解析网页，selenium模块可以启动控制浏览器
2、request.get()返回哪种类型的对象？如何以字符串的方式访问下载的内容
    返回一个response对象，它有一个text属性，包含下载内容的字符串
3、哪个request方法检查下载是否成功？
    下载有问题时raise_for_state()会抛异常
4、如何取得request响应的http状态码？
    Response对象的status_code属性包含了HTTP状态
5、如何将Requests响应保存到文件？
    以‘wb’，即‘写二进制’模式在计算机上打开新文件后，利用一个for循环迭代遍历response对象的iter_ci=ontent()方法，
    将各段写入该文件。
    如：saveFile = open（'filename.html','wb')
        for chunk in res.iter_content(100000):
            savefile.write(chunk)
    
6、打开浏览者开发工具，快捷键是什么？
      F12
7、在开发者工具中，如何查看页面上特定元素的HTML?
    右键点击页面上的元素，并从菜单中选择InspectElement
8、要找id属性为main的元素，css选择器的字符串是什么？
    '#main'
9、要找css类为highlight的元素，css选择器的字符串是什么？
    '.heiglight'
10、要找一个<div>元素中所有的<div>元素，css选择器的字符串是什么？
    'div div'
11、要找一个<button>元素，它的value属性被设置为favorite，css选择器的字符串是什么？
    'button[value="favorite"]'
12、假定你有一个beautifulsoup 的Tag对象保存在变量spam中，针对的元素是<div>Hello world!</div>.
如何从这个Tag对象中取得字符串'Hello world!'?
    spam.getText()
13、如何将一个BeautifulSoup的Tag对象的所有属性保存到变量linkElem中？
    linkElem.arrs
14、运行import selenium没有效果。如何正确的导入selenium模块？
    from selenium import webdriver
15、find_element_*和find_elements_*方法之间的区别是什么？
    find_element_*返回一个WebElement对象，代表页面中匹配查询的第一个元素
    find_elements_*返回webElement_*对象的列表，包含所有匹配的元素。
16、Selenium的WebElement对象有哪些方法来模拟鼠标点击和键盘敲击？
    click()、send_keys()
17、你可以在Submit按钮的WebElement对象上调用send_keys(Keys.ENTER),但是利用selenium，还有
什么更容易的方法提交表单？
    submit()
18、利用selenium如何模拟点击浏览器的‘前进’、‘返回’、和‘刷新’按钮？
    browser.dorward()点击前进
    browser.refresh()刷新
    browser.back()返回