#-*- coding:utf-8 -*-
import pandas as pd
from tqdm import tqdm
from source codes.mk import *
        
#Transformation of Plink result file
def conver_ld2csv(data):
    LD_data=[]
    for i in tqdm(range(len(data))):
        if i==0:
            columns=data[i].split()
            continue
        else:
            LD_data.append(data[i].split())
    return LD_data,columns


if __name__ == '__main__':
    file=u"scz"
    path=u"../LD/"
    mkdir(path)
    try:
        f=open(u"../plink-1.07-dos/"+file+u".ld",u"r")
        data=f.readlines()
        data,columns=conver_ld2csv(data)
        LD_data=pd.DataFrame(data,columns=columns)
        LD_data.to_csv(path+file+u"_LD.csv",index=None)
    finally:
        if f:
            f.close()