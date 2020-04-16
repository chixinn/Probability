#!/usr/bin/python3

##利用python 检验数据的正态分布性
##完成目标：1-生成随机数；2-生成符合正态分布的随机数 3-随机数检验
##scipy.stats.kstest
from scipy import stats
import numpy as np
##input: n,mu,sigma

n=input("input n")
mu=input("input mu")
sigma=input("input sigma")


array=np.random.normal(size=(mu,sigma))##only std;


##read_data
##cal_expectation
##cal_std
