import pandas as pd
from tqdm import tqdm
import numpy as np
from .mk import *

#Screening suitable linkage disequilibrium
def select_snp(data,percent):

    r2_min_25 = data[data[u"R2"] <= percent]
    r2_max_25 = data[data[u"R2"] > percent]

    snp_max_25_a = set(r2_max_25[u"SNP_A"])
    snp_max_25_b = set(r2_max_25[u"SNP_B"])
    snp_max_25 = snp_max_25_a | snp_max_25_b

    snp_min_25_a = set(r2_min_25[u"SNP_A"])
    snp_min_25_b = set(r2_min_25[u"SNP_B"])
    snp_min_25 = snp_min_25_a | snp_min_25_b
    return np.array(list(snp_min_25-snp_max_25))



if __name__ == '__main__':
    name=u"control"
    #name=u"scz"
    #name=u"bpd"
    
    path=u"../asm_ld/"
    mkdir(path)
    percent=0.25

    data = pd.read_csv(u"../LD/" + name + u"_LD.csv", encoding="gbk")
    snp=select_snp(data,percent)

    data=pd.DataFrame(snp,columns=[u"snpid"])
    data.to_csv(path+name+u"_asm_ld.csv",index=None)
