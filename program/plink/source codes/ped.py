#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from tqdm import tqdm
from .mk import *
        
        
#Create ped format file 
def creat_ped(map_info_part,genotype):
    ID_REF=np.array(genotype[u"ID_REF"])

    genotype=genotype.drop([u"ID_REF"], axis=1)
    print (u"start create part ped data")
    family_id=np.array(genotype.columns)
    number_of_family=len(family_id)
    Individual_ID=np.ones(number_of_family,dtype=np.int)
    Paternal_ID=np.zeros(number_of_family,dtype=np.int)
    Maternal_ID=np.zeros(number_of_family,dtype=np.int)
    Sex=np.ones(number_of_family,dtype=np.int)
    Phenotype=np.ones(number_of_family,dtype=np.int)
    temp_ped=pd.DataFrame()
    temp_ped[u"family_id"]=family_id
    temp_ped[u"Individual_ID"]=Individual_ID
    temp_ped[u"Paternal_ID"]=Paternal_ID
    temp_ped[u"Maternal_ID"]=Maternal_ID
    temp_ped[u"Sex"]=Sex
    temp_ped[u"Phenotype"]=Phenotype
    print (u"success creat part ped")


    print (u"start covert genotype !")
    for i in tqdm(genotype.index):
        allele_A=map_info_part.ix[i,u"Allele A"]
        allele_B=map_info_part.ix[i,u"Allele B"]
        replace_dict={u"AA": allele_A+u" "+allele_A, u"AB": allele_A+u" "+allele_B, u"BB": allele_B+u" "+allele_B}
        genotype.iloc[i].replace(replace_dict,inplace = True)
    print (u"success convert !")
    new_genotype=pd.DataFrame(np.mat(genotype).T,columns=ID_REF)
    ped=pd.concat([temp_ped,new_genotype],axis=1)

    print (u"creat ped success !")
    return ped

if __name__ == '__main__':
    name=u"control"
    #name=u"scz"
    #name=u"bpd"
    map_info=pd.read_csv(u"../map_info/"+name+u"_info.csv",encoding=u"gbk")
    map_info_part=map_info[[u"index",u"Allele A",u"Allele B"]]

    genotype=pd.read_csv(u"../../gwas/genotype/"+name+u"_genotype.csv",encoding=u"gbk")
    genotype=genotype.loc[map_info_part[u"index"]].reset_index(drop=True)
    ped=creat_ped(map_info_part,genotype)
    path=u"../ped/"
    mkdir(path)
    ped.to_csv(path+name+u".ped",index=None,header=None,sep="\t")