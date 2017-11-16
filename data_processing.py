# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:18:43 2017

@author: neo
"""

#将两个文件夹中的所有文件读取，并写入学号，保存到一个csv文件中去

import pandas as pd
import os
#cutoff 函数从文件夹中的各个文件截取
def cutoff(path, data =[]):
    from tqdm import tqdm#需要导入tqdm实现进度条
    pathlist = os.listdir(path)
    for i in tqdm(pathlist):
        f = pd.read_csv(path+"//"+i)
        f["学号"] = i[:9]
        f = f[['本方户名','学号','事件名称','对方户名','交易额','流水时间']]
        data.append(f)
    print("成功导入了{}文件夹下所有文件".format(path[(len(path) - path[::-1].find('/')):]))
    return data

def inputData(output = False):
    data=[];
    path1 = r"/Users/neo/Desktop/11csv"
    path2 = r"/Users/neo/Desktop/12csv"
    cutoff(path1,data)
    cutoff(path2,data)
    data = pd.concat(data,ignore_index = True)
    print("成功生成data数据")
    if output == True:
        data.to_csv(r"/Users/neo/Desktop/cutoff.csv",index = False, encoding = 'utf-8')
        print("成功导出data文件")
    return data
datas = inputData(output = True)
#by neo
