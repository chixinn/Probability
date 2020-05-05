#!/usr/bin/python3

##利用python 检验数据的正态分布性
##完成目标：1-生成随机数；2-生成符合正态分布的随机数 3-随机数检验
##scipy.stats.kstest
#k-s 检验
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
##input: n,mu,sigma

n=input("input n")
mu=input("input mu")
sigma=input("input sigma")

#生成数据集

#利用numpy.random.normal()函数
#np.random.normal(loc=0.0, scale=1.0, size=None),loc为均值，scale为标准差。
#绘制样本的直方图和概率密度函数
array=np.random.normal(mu,sigma,1000)
count,bins,ignored=plt.hist(array,30,density=True)
plt.plot(bins,1/(sigma*np.sqrt(2*np.pi))*n.exp(-(bins-mu)**2/(2*sigma**2)),linewidth=2,color='r')
plt.show()

#正态性检验

#Example,判断p-value的值是否小于0.05
x1=np.linespace(-15,15,9)#创建等差数列，非正态
print(stats.kstest(x1,'norm'))
#使用numpy生成符合正态分布的随机数
np.random.seed(1000)
x2=np.random.randn(100)
D,p_value=stats.kstest('norm',False,N=100)#返回一个或一组样本，具有标准正态分布
print(p_value)
if (p_value>0.05):
    print("Not a Normal Distribution")
else 
    print("Is a Normal Distribution")




##read_data
##cal_expectation
##cal_std
