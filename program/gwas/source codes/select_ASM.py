#-*- coding:utf-*-
import pandas as pd
from tqdm import tqdm
from source codes.pwl import PWL
from source codes.adjust_p_value import *
from source codes.mk import *
        
def select_signal(columns):
    new_clumns=[]
    for item in columns:
        new_clumns.append(item+ u"_signal")
    return np.array(new_clumns)

#Finish filtering ASM data
def ASM_SNP(input_file_name,output_file_name):
    screen=pd.read_csv(u"../screen/"+input_file_name+u"_screen.csv",encoding=u"gbk",low_memory=False)
    index=screen[u"index"]

    genotype_data=pd.read_csv(u"../genotype/"+input_file_name+u"_genotype.csv",encoding=u"gbk",low_memory=False)
    genotype_data=genotype_data.loc[index]

    signal_data=pd.read_csv(u"../signal/"+input_file_name+u"_signal.csv",encoding=u"gbk",low_memory=False)
    
    signal_data=signal_data.loc[index]

    genotype_data=genotype_data.drop(u"ID_REF", axis=1)
    signal_data=signal_data.drop(u"ID_REF", axis=1)

    replace_dict = {u"AA": 0, u"AB": 1, u"BB": 2}

    pvalue=[]
    flag=[]
    for i in tqdm(index):
        label = genotype_data.loc[i]
        x_item=set(label)
        if len(x_item)<=2:
            pvalue.append(1)
            flag.append(0)
            continue

        y = np.array(signal_data.loc[i])

        x = label.replace(replace_dict)
        flg, plv = PWL(x, y)

        pvalue.append(plv)
        flag.append(flg)
    fdr = p_adjust_bh(pvalue)
    result = pd.DataFrame()
    result[u"pvalue"] = np.array(pvalue)
    result[u"fdr"] = fdr
    result[u"flag"] = np.array(flag)
    asm = pd.concat([screen, result], axis=1)

    asm = asm[(asm[u"fdr"] < 0.01)& (asm[u"flag"] >0) ]
    path=u"../ASM_SNP/"
    mkdir(path)
    asm.to_csv( path+ output_file_name + u"_asm.csv", index=None)





if __name__ == '__main__':
    name=u"control"
    #name=u"scz"
    #name=u"bpd"
    ASM_SNP(name,name)