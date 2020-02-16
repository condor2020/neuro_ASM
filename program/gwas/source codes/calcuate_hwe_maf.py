#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from scipy.stats import chisquare
from tqdm import tqdm
from source codes.mk import *
        
        
#Calculate HWE and MAF
def Get_AA_AB_BB_Hardy_Weinberg_MAF(input_file_name,output_file_name):
    data=pd.read_csv(u"../genotype/"+input_file_name,encoding=u"gbk")
    Affyid = data[u"ID_REF"]
    data = data.drop(u"ID_REF", axis=1)
    MAF=[]
    HW=[]
    for i in tqdm(data.index):
        aa=0
        ab=0
        bb=0
        count=data.loc[i].value_counts()
        for item in count.index:
            if item ==u"AA":
                aa=count[item]
                continue
            if item == u"AB":
                ab=count[item]
                continue
            if item == u"BB":
                bb=count[item]

       
        sum=float(aa+ab+bb)
        p = (2 * aa + ab) / (2 * sum)
        q = 1 - p
        # Calculate MAF
        if p >= q:
            maf = q
        else:
            maf = p
        MAF.append(maf)
        #Calculate HWE
        exp_aa = p ** 2 * sum
        exp_ab = 2 * p * q * sum
        exp_bb = q ** 2 * sum

        obs=[]
        exp=[]
        if exp_aa!= 0:
            obs.append(aa)
            exp.append(exp_aa)
        if exp_ab !=0:
            obs.append(ab)
            exp.append(exp_ab)
        if exp_bb != 0:
            obs.append(bb)
            exp.append(exp_bb)
        chi_scp, p_scp = chisquare(obs, f_exp=exp)
        if np.isnan(p_scp):
            HW.append(0)
        else:
            HW.append(p_scp)

    result=pd.DataFrame()
    result[u"ID_REF"]=Affyid
    result[u"HWE"]=HW
    result[u"MAF"]=MAF
    path=u"../HWE_MAF/"
    mkdir(path)
    result.to_csv(path+output_file_name+".csv",index=None)


if __name__ == '__main__':
    control=u"control_genotype.csv"
    #scz=u"scz_genotype.csv"
    #bpd=u"bpd_genotype.csv"
    Get_AA_AB_BB_Hardy_Weinberg_MAF(control,u"control")
