#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from source codes.mk import mkdir

#Process SNP ID mapping table
data=pd.read_table(u"../data/GPL6801-4019.txt",encoding=u"gbk",sep="\t",low_memory=False)
new_data=data.drop([u"RANGE_GB",u"RANGE_START",u"RANGE_STOP",u"STRAND"],axis=1)
new_data=new_data[(new_data[u"Chromosome"]!=u"---") & (new_data[u"Physical Position"]!=u"---")].dropna()
path=u"../GPL/"
mkdir(path)
new_data.to_csv(path+u"GPL.csv",index=None)