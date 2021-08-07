import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/23511/IBI1_2020-21/Practice7")
reports = pd.read_csv("report.csv")
print(reports.loc[0:11:2, :])

j = 1
z = 1
i = 1

while i <= 211:
    if reports.loc[i, "1、您的性别？"] == '男':
        if reports.loc[i,'3、您会仔细阅读各软件、平台的隐私条款吗？'] == '会':
            j = j+1
        if reports.loc[i,'3、您会仔细阅读各软件、平台的隐私条款吗？'] == '不会':
            z = z+1
    i=i+1
print(j)

#labels='会','不会'
#sizes = [j,z]
#explode = (0,0)
#colors = ['red' , 'blue']
#plt.title('男生仔细阅读各软件、平台的隐私条款的情况')
#plt.pie(bili, explode=explode, labels=labels, autopct='%1.1f%%', shadow= False, startangle=90)
#plt.axis('equal')
#plt.show()