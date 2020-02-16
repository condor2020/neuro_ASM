#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from source codes.mk import *

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)

    if not isExists: 
        os.makedirs(path)
        print(path + ' success')
        return True
    else:  
        print(path + ' exist')
        return False

#Extract signals of all ASM loci
print (u"start program !")
bpd_data=pd.read_csv(u"../../plink/asm_ld/bpd_asm_ld.csv",low_memory=False)
scz_data=pd.read_csv(u"../../plink/asm_ld/scz_asm_ld.csv",low_memory=False)
control_data=pd.read_csv(u"../../plink/asm_ld/control_asm_ld.csv",low_memory=False)

asm_bpd=bpd_data[u"snpid"]
asm_scz=scz_data[u"snpid"]
asm_control=control_data[u"snpid"]
print (u"read all asm snps !")

bpd_info=pd.read_csv(u"../../gwas/ASM_SNP/bpd_asm.csv",low_memory=False)
bpd_dict=dict(zip(bpd_info[u"SNP_ID"],bpd_info[u"index"]))

scz_info=pd.read_csv(u"../../gwas/ASM_SNP/scz_asm.csv",low_memory=False)
scz_dict=dict(zip(scz_info[u"SNP_ID"],scz_info[u"index"]))

control_info=pd.read_csv(u"../../gwas/ASM_SNP/control_asm.csv",low_memory=False)
control_dict=dict(zip(control_info[u"SNP_ID"],control_info[u"index"]))

print (u"create all dict")

bpd_index=[]
for i in asm_bpd:
    bpd_index.append(bpd_dict[i])

scz_index=[]
for i in asm_scz:
    scz_index.append(scz_dict[i])

control_index=[]
for i in asm_control:
    control_index.append(control_dict[i])

print (u"conver snpid to index !")

all_index=np.array(list(set(bpd_index) | set(scz_index) | set(control_index)))

all_signal=pd.read_csv(u"../../gwas/signal/all_signal.csv",low_memory=False)

new_signal=all_signal.iloc[all_index].reset_index(drop=True)

print (u"select singnal all right !")

title_data=pd.read_csv(u"../../sample_type/result/sample_type.csv")

bipolar=title_data[title_data[u"sample_type"]==u"bipolar"]
bipolar_columns=np.array(bipolar[u"sample_id"])
bipolar_new_columns=np.array(bipolar[u"id_type"])

schizophrenia=title_data[title_data[u"sample_type"]==u"schizophrenia"]
schizophrenia_columns=np.array(schizophrenia[u"sample_id"])
schizophrenia_new_columns=np.array(schizophrenia[u"id_type"])

control=title_data[title_data[u"sample_type"]==u"control"]
control_columns=np.array(control[u"sample_id"])
control_new_columns=np.array(control[u"id_type"])

ID_REF=new_signal[u"ID_REF"]
new_control=new_signal[control_columns]
new_control.columns=control_new_columns

new_scz=new_signal[schizophrenia_columns]
new_scz.columns=schizophrenia_new_columns

new_bpd=new_signal[bipolar_columns]
new_bpd.columns=bipolar_new_columns

result=pd.concat([ID_REF,new_control,new_scz,new_bpd],axis=1)


print (u"replace title complete !")

path=u"../all_signal"
mkdir(path)
result.to_csv(path+"/all_signal.csv",index=None)




