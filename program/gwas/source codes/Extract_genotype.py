#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from .mk import *
        
#Complete the extraction of genotype of different disease types
def genotype(input_file_name,output_file_name):
    print (u"start reading genotype data！")
    data=pd.read_table(u"../data/"+input_file_name,encoding=u"gbk",low_memory=False,sep="\t")

    Affyid=data[u"ID_REF"]
    data=data.drop(u"ID_REF",axis=1)

    column=data.columns

    genotype_columns=[]
    for i in range(len(column)):
        if i%2 ==0:
            genotype_columns.append(column[i])

    print (u"Recognition of corresponding column of prototype！")
    genotype_data=data[genotype_columns]

    data=pd.concat([Affyid,genotype_data],axis=1)
    print (u"Merger success!")
    path=u"../genotype/"
    mkdir(path)
    data.to_csv(path+output_file_name+u"_genotype.csv",index=None)



if __name__ == '__main__':
    control=u"GSE71443_control_Brain_white_crlmm_1.8.11.GEO.snp.tab.txt"
    scz=u"GSE71443_SZ_Brain_white_crlmm_1.8.11.GEO.snp.tab.txt"
    bpd=u"GSE71443_BD_Brain_white_crlmm_1.8.11.GEO.snp.tab.txt"
    genotype(bpd,u"bpd")
    #genotype(scz,u"scz")
    #genotype(control,u"control")