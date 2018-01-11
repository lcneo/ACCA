import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl 

def Extension():   
    f= pd.read_csv("doc/data_final.csv",encoding = 'utf-8')   
    mpl.rcParams['font.sans-serif'] = ['SimHei']                                                                                                                                                                                           
    plt.bar(range(2),f.是否延期.value_counts())                                 
    plt.title('11、12级学生延期分布情况')
    plt.ylabel('学生数量')
    plt.xlabel('是否延期')
    plt.xticks(range(2),['否','是'])
    length = len(f)
    for x,y in zip(range(2),f.是否延期.value_counts()):
        plt.text(x,y+10,str('%.2f%%' % (( y/length) * 100)),ha='center')
    plt.show()
if __name__ == '__main__':
    Extension()

