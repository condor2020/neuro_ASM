#-*- coding:utf-8 -*-
import numpy as np
import pwlf
from scipy.stats import t


#Calculation of piecewise linear regressio
def PWL(x,y):

    x0 = np.array([min(x), 1, max(x)])
    my_pwlf = pwlf.PiecewiseLinFit(x, y)
    my_pwlf.fit_with_breaks(x0)

    my_slopes = my_pwlf.slopes
    pvalue=1
    flag=0
    for i in range(len(my_slopes)):

        xmin = my_pwlf.fit_breaks[i]
        xmax = my_pwlf.fit_breaks[i + 1]
        xtemp = my_pwlf.x_data
        indtemp = np.where(xtemp >= xmin)
        xtemp = my_pwlf.x_data[indtemp]
        ytemp = my_pwlf.y_data[indtemp]
        indtemp = np.where(xtemp <= xmax)
        xtemp = xtemp[indtemp]
        ytemp = ytemp[indtemp]

        x_hat=xtemp
        yhat=np.array(my_pwlf.predict(xtemp),dtype=np.float16)

        n = len(x_hat)
        L_xx=n * np.var(x_hat)

        se = np.array(ytemp,dtype=np.float16) - yhat
        SSE = np.dot(se, se)
        sigma=np.sqrt(SSE/n)
        if sigma==0.0:
            continue

        T=my_slopes[i]*np.sqrt(L_xx)/sigma

        pvl = t.sf(T,n-2)
        if my_slopes[i]!=0:
            flag=flag+1
            if pvalue>pvl:
                pvalue=pvl

    return flag, pvalue

