#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from source codes.mk import *
# Amplify signal strength of all sites
data=pd.read_csv(u"../all_signal/all_signal.csv")

ID_REF=data[u"ID_REF"]

data=data.drop(u"ID_REF",axis=1)

column = data.columns

data=np.mat(data)

row, col = data.shape

data_min=data.min(axis=1)

data_repeat = np.tile(data_min,(1,col))

gwas=(data-data_repeat)*10

gwas=pd.DataFrame(gwas,columns=column)

amplify = pd.concat([ID_REF, gwas], axis=1)

amplify = amplify.round(4)

path=u"../amplify/"

mkdir(path)

amplify.to_csv(path+u"amplify_all.csv", index=None)