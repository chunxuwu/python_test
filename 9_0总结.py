# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:33:39 2018
第九章总结组织文件

@author: NEVERGUVEIP
"""

1、shutil模块用来复制、移动、改名和删除文件
    shutil.copy 
    shutil.move(source,destination),如果移动文件到目标文件夹存在，就移动，如果移动的目标文件夹不存在
    则会发生怪异事件，即move会认为给定的des是文件，而不是文件夹，则原文件被改名为des。目的地文件夹必须存在，
    系统不会自动创建
    shutil.rmtree(path)将删除path处的文件夹，永久性的，不可恢复
    os.rmdir(path)删除path处的空文件夹
    os.unlink(path)删除一个文件
    send2trash 删除文件到垃圾箱

2、遍历目录树
    os.walk(path)
    for foldername,subfoldernames,filenames in os.walk('.'):

    
3、用zipfile模块压缩文件
  【1】读取zip文件
     首先必须创建ZipFile对象，首字母大写，即examoleZip=zipfile.ZipFile()
     exampleZip.namelist()返回ZIP文件中所有文件和文件夹的字符串列表
     spamInfo=exampleZip.getinfo('spam.txt')
     spamInfo.file_size#文件大小
     spamInfo.compress_size#压缩后文件的大小，可以用来求压缩率
  【2】解压zip文件
     先创建一个对象exampleZip=zipfile.ZipFile('example.zip')
                 exampleZip.extractall(path)#解药到path文件夹处，为空时就解压到当前文件夹中
                 
  【3】创建和添加到zip文件
      newZip=zipfile.ZipFile('new.zip','w')
      nweZip.write('spam.txt',compress_type=zipfile.ZIP_DEFLATED)#第二个参数问指定压缩算法
      newZip.close()
4、将带有美国风格日期的文件改名

