# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 10:08:42 2018
第10章总结


@author: NEVERGUVEIP
"""

10.7 习题

1、写一条assert语句，如果变量spam是一个小于10的整数，就出发AssertionError
    #assert  spam < 10 ,'variable spam smalle than 10'
    assert (spam>=10,'the spam variable is less than 10')
2、编写assert语句，如果eggs和bacon 包含的字符串相同就触发，忽略大小写
    #assert lower.eggs() == lower.bacon()
    assert (eggs.lower()!=bacon.lower(),'the eggs and bacon variable are the same'
3、编写一条assert语句总是触发AssertionError
    #assert True
    assert(False,'this assertion always triggers.')
4、为了能调用logging.debug(),程序中必须加入哪俩行代码
    import logging
    logging.basicConfig(level=logging.DEBUG, 
                        format = '%(asctime)s - %(levelname)s - %(message)s')
5、为了让logging.debug()将日志消息发送到名为programLog.txt的文件中，程序必须加入哪俩行代码
    import logging
    logging.basicConfig(filename='programLog.txt',level=logging.DEBUG,
                        format = '%(asctime)s-%(levelname)s-%message)s')
6、5个日志级别是什么
    DEBUG\INFO\WARNING\ERROR\CRITICAL
7、加入一行代码，禁用程序中所有的日志消息
    logging.disable(logging.CRITICAL)
8、显示同样的消息，为什么使用日志比print好
    使用print调试完，需要一个一个的删除掉print，看起来简单，实际很麻烦
    使用日志需要开始写入俩行代码如import logging，logging.basicConfig(////)
    日志禁用时只需要logging.disable(logginf.CRITICAL),就可以禁用
    (禁用日志时不必删除日志函数调用，可以选择禁用低级日志消息、可以创建日志文本，日志提供了时间戳)
9、调试控制窗口中的step、Over、Out有什么区别
    step是步进调试、Over与step类似，只是当over的下一条语句是函数调用时，调试将不进入
    函数内部，函数的代码将迅速执行，调试器将在函数返回后停止、Out是全速执行函数内的代码
    直到函数返回结果，从当前函数中跳出来。
10、在点击调试控制窗口的Go按钮后，调试器为何会停下来
    GO导致程序正常执行到结束或到达一个端点
11、什么是断点
    断点是设置在特定的代码行，当程序执行到达该行时，使调试器停下来
12、如何设置断点
    双击特定代码的开头处
    
    