"""
there is no filetype format for markdown file with images now, this script archive the markdown and images to a file end with ".mdzip" using zip compress.

"""

# -*- coding: utf-8 -*-

import os
import zipfile
import subprocess
import sys


import win32api,win32con
#import traceback

# TODO
### serious  连续打开时，会造成md文件删除而未保存 DONE

### TODO set for typora

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'test.mdzip'
    filename = 'readme.md'
#print(filename)
# for test !!

#filename = "aa.mdzip"
filename = os.path.basename(filename)
#print(filename)

mdFilename = ''
zipFilename = ''
mdDirFilename = ''

if os.path.splitext(filename)[1] == '.md':
    zipFilename = filename.strip(".md") + '.mdzip'
    mdFilename = filename
    mdDirFilename = '_' + filename.strip(".md") + '_mdzip'
    if os.path.exists(mdDirFilename) == False:
        os.mkdir(mdDirFilename)
#    if os.path.exists(filename):
#        os.rename(filename,mdDirFilename+'/'+filename)

    #print( "typora " + filename)
    openExe = subprocess.Popen("typora " + mdFilename)
    openExe.wait() #此函数对typora无效，原因未知，对windows的notepad有效

elif os.path.splitext(filename)[1] == '.mdzip':
    #mdDirFilename = '_' + filename.strip(".mdzip") + '_mdzip'
    zipFilename = filename
    mdFilename = filename.strip('.mdzip') + '.md'
    mdDirFilename = '_' + filename.strip(".mdzip") + '_mdzip'

    # 如果文件夹或文件已经存在  TODO 给予是否覆盖的选择
    if  os.path.exists(mdDirFilename) :
        win32api.MessageBox(0,"ERROR: 已存在 \""+mdDirFilename+"\" 文件夹","md_open Error", win32con.MB_OK)
        sys.exit(0)

    if  os.path.exists(mdFilename):
        win32api.MessageBox(0,"ERROR: 已存在 \""+mdFilename+"\" 文件夹","md_open Error", win32con.MB_OK)
        sys.exit(0)


    ## 需要判断是否已经存在md文件，如果存在抛异常
    zfile = zipfile.ZipFile(filename,'r')
    for fname in zfile.namelist():
        #print(fname)
        zfile.extract(fname)
    zfile.close()


        #raise Exception("重复打开")  # 重复打开判断有更好的方式？

        # TODO 弹出错误对话框

    if os.path.exists(mdDirFilename) == False:
        os.mkdir(mdDirFilename)

    if os.path.exists(mdFilename):
#        print(233)
        openExe = subprocess.Popen("typora " + mdFilename) # 这个函数又能用了......
        #  TODO 设置打开默认的md程序
        openExe.wait()

#print(11)
#
#from win32gui import *
#import time
#
#isTyporaClosed = False
#time.sleep(5) # 避免软件打开延时
##print('mdfilename:  ' + mdFilename )
#while isTyporaClosed == False:
#    print(111)
#    titles = set()
#    def foo(hwnd,nouse):
#        if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
#            titles.add(GetWindowText(hwnd))
#    EnumWindows(foo, 0)
#
#    isTyporaClosed = True
#    #lt = [t for t in titles if t]
#    #print(titles)
#    for t in titles:
#        if t == mdFilename + " - Typora" or t == mdFilename + "• - Typora" :
#            isTyporaClosed = False
#
#    time.sleep(1)
#    print(222)
#    #print(isTyporaClosed)
#
#
#print(1)

if os.path.exists(zipFilename):
    os.remove(zipFilename)


# 压缩文件
compressFile = zipfile.ZipFile(zipFilename, 'w')
compressFile.write(mdFilename)
## 压缩文件目录时需要遍历，否则文件夹中的内容不会添加
for root, dirlist, files in os.walk(mdDirFilename):
    for filename in files:
        compressFile.write(os.path.join(root,filename))
#compressFile.write(mdDirFilename)
compressFile.close()


# 清理文件
os.remove(mdFilename)
#os.removedirs(mdDirFilename)
import shutil
shutil.rmtree(mdDirFilename)


print( 'over' )
