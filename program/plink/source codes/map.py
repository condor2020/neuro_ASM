#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from .mk import *
        
#Create map format file and map information
def project_GPL(ASM_SNP,outputfilename):

    row,col=ASM_SNP.shape
    print (u"start creat map file!")
    Chromosome=ASM_SNP[u"Chromosome"]
    SNP_ID=ASM_SNP[u"SNP_ID"]
    Genetic_distance = np.zeros(row, dtype=np.int)
    Basepair_position=ASM_SNP[u"Physical Position"]
    MAP = pd.DataFrame()
    MAP[u"chrom"] = Chromosome
    MAP[u"snpid"] = SNP_ID
    MAP[u"distance"] = Genetic_distance
    MAP[u"position"] = Basepair_position
    path=u"../map/"
    mkdir(path)
    MAP.to_csv(path + outputfilename + u".map", index=None, header=None, sep="\t")
    print (u"map creat sucess !")

    MAP_INFO=ASM_SNP[[u"SNP_ID",u"ID_REF",u"index",u"Allele A",u"Allele B"]]
    path=u"../map_info/"
    mkdir(path)
    MAP_INFO.to_csv(path + outputfilename + u"_info.csv", index=None)
    print (u"map info creat sucess!")



if __name__ == '__main__':
    name=u"control"
    inputfilename=name+u"_asm.csv"
    outputfilename=name
    asm=pd.read_csv(u"../../gwas/ASM_SNP/"+inputfilename,low_memory=False)
    project_GPL(asm,outputfilename)