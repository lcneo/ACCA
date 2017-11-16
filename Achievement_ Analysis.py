#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 15:42:48 2017

@author: neo
"""

import pandas as pd
import warnings
from tqdm import tqdm
#输入成绩文件的路径，导入文件对成绩进行初步的筛选;
#去除其中课程属性代码为3的项，去除选课人数少于5的项，去除标准差等于零的项;
warnings.filterwarnings("ignore")
def sift(path, output = False):
    f = pd.read_csv(path)
    #fun1(f)
    f = f[f.xh//10000000 >10]
    #去除课程属性代码为3的课程
    f = f[f['KCSXDM'] != 3]
    #去除选课人数少于5的课程
    f.index = f['KCH']#课程号作为index,进行bool索引
    #kc = f['KCH'].value_counts()>5
    #f = f[kc[f['KCH']]]
    #去除标准差为0的课程
    course = f['KCCJ'].groupby(f['KCH'])
    std = course.std()!=0
    f = f[std[f['KCH']]]
    #将补考成绩转换为60分
    f['KCCJ'][f['KSSJ']%1000//100 == 9] =60
    f['KCCJ'][f['KSSJ']%1000//100 == 3] =60
    f.index = range(len(f))
    if output == True:
        f.to_csv(path[:len(path) - path[::-1].find('/')]+'筛选后的成绩.csv',\
                      index = False,encoding = 'utf-8')
        print("成功输输出筛选后的成绩")
    return f

#输入文件路径读取成绩表格，得到课程的选课人数，平均值，成绩最大值；
#成绩最小值，标准差等数据。输出结果的xlsx文件;
def score(f, output = False):
    course = f['KCCJ'].groupby(f['KCH'])#使用groupby函数按组求得各值，concat axis=1横向拼接起来
    key = ['课程号','选课人数','平均成绩','成绩最大值','成绩最小值','标准差']
    element = [pd.Series(f['KCH'].unique(),index = f['KCH'].unique()),\
               pd.Series(f['KCH'].value_counts(),index = f['KCH'].unique()),\
               course.mean(),course.max(),course.min(),course.std()]
    data = pd.concat(element,keys = key,axis = 1)
    data.index = range(len(data))
    kcm,xf,lb = [],[],[]
    for i in tqdm(data.课程号):
        kcm.append(list(f['KCM'][f.KCH ==i])[0])
        xf.append(list(f['XF'][f.KCH ==i])[0])
        lb.append(list(f['KCSXDM'][f.KCH ==i])[0])
    data['学分'] = xf
    data['课程类别'] =lb
    data['课程名'] = kcm
    #data = data[['课程号','选课人数','平均成绩','成绩最大值','成绩最小值','标准差']]
    if output == True:
        data.to_csv('/Users/neo/Desktop/按课程分析结果.csv',index = False,\
                    encoding = 'utf-8')
        print("成功输出按课程分析结果")
    return data

#对源文件中的信息进行统计
def fun1(f):
    elements = [len(f['KCH'].value_counts()),len(f['xh'].value_counts()),1]
    print(elements)
    pass

#导入项返回系数成绩
def results(f):
    a = pd.cut(f.KCCJ,[-1, 59, 69, 79, 89, 100],labels = [1,2,3,4,5])
    data = []
    for i in range(1,6):
        data.append(f.ix[list(a[a==i].index)]['KCCJ']*i)
    data = pd.concat(data)
    f['cj*xs'] = data
    f['cj*xf*xs'] = f['cj*xs']*f['XF']
    cj = f['cj*xf*xs'].groupby(f['xh']).sum()
    xf = f['XF'].groupby(f['xh']).sum()
    a = cj/xf
    return a
f = sift('/Users/neo/Desktop/201012级成绩.csv')
#data = results(f)
#从总数据中截取出每一学期的数据，并去除一些无用数据项
def term(f,i):
    bins = [0,20120310,20120915,20130310,20130910,20140311,20140920,20150316,20150925,20160302,20160605]
    key = [1,2,3,4,5,6,7,8,9,10]  
    f = f[pd.cut(f.KSSJ,bins,labels = key) == i]
    #去除选课人数少于5的课程
    f.index = f['KCH']#课程号作为index,进行bool索引
    kc = f['KCH'].value_counts()>5
    f = f[kc[f['KCH']]]
    f.index = range(len(f))

    return f
f = sift('/Users/neo/Desktop/201012级成绩.csv')
#每学期成绩通过公式计算后进行拼接
def allResults(f):
    data,name = [],[]
    for i  in range(1,11):
        data.append(results(term(f,i)))
    key = ['2012上','2012下','2013上','2013下','2014上','2014下','2015上','2015下','2016上','2016下']
    data = pd.concat(data,axis = 1,keys = key)
    data['学号']=data.index
    for i in data.index:
        name.append(list(f['xm'][f.xh == i])[0])
    data['姓名'] =name
    data = data[['学号','姓名']+key]
    data.index = range(len(data))
    print(data)
    return data
#对每学期的课程的课程信息分析后拼接
def allscore(f):
    #data= []
    pass
    
data = allResults(f)
#by neo
