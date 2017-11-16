# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 18:25:53 2017
文件转换为csv
@author: neo
"""
import pandas as pd
import os

path,dataName = [],[]
pathData1 =  r"C:\Users\Administrator\Desktop\data\1150"
#获取11文件夹下所有.xls文件的路径存入
path1 = os.listdir(pathData1)
for i in path1:
    path11 = os.listdir(pathData1+'\\'+i)
    for j in path11:
        if j[-1] == 's':
            path.append(pathData1+'\\'+i+'\\'+j)
            dataName.append(j[:-3]+'csv')
#获取12文件夹下所有.xls文件的路径
pathData2 =  r"C:\Users\Administrator\Desktop\data\1250"
path2 = os.listdir(pathData2)
for i in path2:
    path21 = os.listdir(pathData2+'\\'+i)
    for j in path21:
        if j[-1] == 's':
            path.append(pathData2+'\\'+i+'\\'+j)
            dataName.append(j[:-3]+'csv')
        elif j[-1] != 's' and j[-1] != 't':
            path22 = os.listdir(pathData2+'\\'+i+'\\'+j)
            for k in path22:
                if k[-1] == 's':
                    path.append(pathData2+'\\'+i+'\\'+j+'\\'+k)
                    dataName.append(k[-3]+'csv')
#文件转换为csv格式存储在csv文件夹中
def trscsv():
    count =0
    long = len(path)
    for i in path:
        f = pd.read_excel(i)
        f.to_csv(r"C:\Users\Administrator\Desktop\csv\\"+dataName[count],index=False,encoding = 'utf-8')
        count +=1
        print("{}/{}".format(count,long))
#by neo
