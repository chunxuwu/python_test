# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:10:15 2018
9.5  项目：将一个文件夹备份到一个 ZIP 文件 

@author: NEVERGUVEIP
"""
#! python3

import zipfile,os

def backupToZip(folder):
    #backup the entire contents of 'folder' into a ZIP file
    
    folder = os.path.abspath(folder)
    os.chdir(folder)
    #figure out the filename this code should use based on
    #what files already exist.   
    number = 1    
    #从1循环检查文件名存不存在，_1.zip,_2.zip，，防止备份以前的备份文件
    while True:
        zipFilename = os.path.basename(folder) +'_'+str(number)+'.zip'
        if not os.path.exists(zipFilename):
            break
        number = number +1
        
        
    #creat the zip file
    print('creating %s...'%(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename,'w')
    
    #TODO: walk the entire folder tree and compress the files in each folder.    

    for foldername,subfolders,filenames in os.walk(folder):#
        
        print('adding files in %s...'%(foldername))       
        #add the current folder to the zip file.
        backupZip.write(foldername)
        #add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue# don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername,filename))
                        
    backupZip.close()   
    print('......Done......')

#backupToZip(r'C:\Users\NEVERGUVEIP\Documents\GitHub\python_test')
backupToZip('.')
        
