#-*- coding:utf-8 -*-
import numpy as np
from numpy.linalg import svd

#calculate NSVA
def sva_method(data):
    u, s, vt = svd(data)
    explanation_ratio = s[0] / np.sum(s)*100.0
    contribution_index=np.argsort(u[:,0])
    contribution=-u[contribution_index,0].round(5)
    return contribution_index,contribution,explanation_ratio



