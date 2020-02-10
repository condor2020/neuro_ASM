#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from .sva import *
from .mk import *

#Calculate the importance of each site
data=pd.read_csv(u"../amplify/amplify_all.csv")

ID_REF=data[u"ID_REF"]

data=data.drop(u"ID_REF",axis=1)

contribution_index,contribution,explanation_ratio=sva_method(data)

ID_REF=ID_REF.iloc[contribution_index]
data=data.iloc[contribution_index]

GPL=pd.read_csv(u"../../GPL/GPL/GPL.csv",low_memory=False)

GPL_dict=dict(zip(GPL[u"ID"],GPL[u"SNP_ID"]))
snpid=[]
for item in ID_REF:
    snpid.append(GPL_dict[item])


df=pd.DataFrame()
df[u"ID_REF"]=np.array(ID_REF)
df[u"snpid"]=np.array(snpid)
df[u"index"]=contribution_index
df[u"contribution"]=contribution
df.to_csv(u"../amplify_sva/amplify_sva_info.csv",index=None)

result=pd.concat([ID_REF,data],axis=1)
path=u"../amplify_sva"
mkdir(path)
result.to_csv(path+u"amplify_sva_all.csv",index=None)




