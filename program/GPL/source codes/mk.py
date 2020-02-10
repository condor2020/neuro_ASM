#-*- coding:utf-8 -*-
import os

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