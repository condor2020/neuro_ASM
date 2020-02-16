#-*- coding:utf-8 -*-
import pandas as pd
from source codes.mk import *
        
#Complete the extraction of methy signal of different disease types
def signal(input_file_name,output_file_name):
    print (u"start reading genotype data！")

    data=pd.read_table(u"../data/"+input_file_name,encoding=u"gbk",low_memory=False,sep="\t")

    Affyid=data[u"ID_REF"]
    data=data.drop(u"ID_REF",axis=1)

    column=data.columns

    genotype_columns=[]
    signal_columns={}
    for i in range(len(column)):
        if i%2 ==0:
            genotype_columns.append(column[i])
            signal_columns[column[i+1]]=column[i]+u"_signal"
    data=data.drop(genotype_columns,axis=1)
    signal_data=data.rename(columns=signal_columns)

    data = pd.concat([Affyid, signal_data], axis=1)

    print (u"Merger success!")
    path=u"../signal/"
    mkdir(path)
    data.to_csv(path+output_file_name+u"_signal.csv",index=None)



if __name__ == '__main__':
    all=u"GSE71443_control+case_Brain_white_crlmm_1.8.11.GEO.methy.tab.txt"
    control = u"GSE71443_control_Brain_white_crlmm_1.8.11.GEO.methy.tab.txt"
    scz = u"GSE71443_SZ_Brain_white_crlmm_1.8.11.GEO.methy.tab.txt"
    bpd = u"GSE71443_BD_Brain_white_crlmm_1.8.11.GEO.methy.tab.txt"
    signal(bpd,u"bpd")