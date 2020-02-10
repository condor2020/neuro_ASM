#-*-coding:utf8 -*-
import numpy as np

#Benjamini-Hochberg p-value correction for multiple hypothesis testing.

def p_adjust_bh(p):
    
    pvalue=np.array(p)

    rank=np.argsort(-pvalue)+1

    qvalue=pvalue*len(pvalue)/rank

    return qvalue



