#-*- coding:utf-8 -*-
import pandas as pd
from source codes.mk import *

GPL=pd.read_csv(u"../../GPL/GPL/GPL.csv",encoding="gbk",low_memory=False)

#Complete SNP ID mapping and noise data filtering
def screen_HWE_MAF_INFO(input_file_name,output_file_name):
    data=pd.read_csv("../HWE_MAF/"+input_file_name+".csv",encoding=u"gbk")
    data=data[(data[u"HWE"]>10**(-10)) & (data[u"MAF"]>0.05)]
    data[u"index"]=data.index
    filter= pd.merge(data,GPL,left_on=u"ID_REF",right_on="ID")
    filter=filter.drop(u"ID", axis=1)
    path=u"../screen/"
    mkdir(path)
    filter.to_csv(path+output_file_name+"_screen.csv",index=None)

if __name__ == '__main__':

    screen_HWE_MAF_INFO("control","control")
    screen_HWE_MAF_INFO("scz","scz")
    screen_HWE_MAF_INFO("bpd","bpd")