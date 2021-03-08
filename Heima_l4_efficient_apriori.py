#create by Murphy 2021/03
#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from efficient_apriori import apriori
import time,datetime
# from mlxtend.frequent_patterns import apriori
# from mlxtend.frequent_patterns import association_rules
#数据加载
data=pd.read_csv(r'D:\黑马课程\第四课\Market_Basket_Optimisation.csv',header=None)
print(data)
print(data.shape)#(7501, 20)
#按行遍历
transactions=[]
for i in range(data.shape[0]):
    temp=[]
    #按列遍历
    for j in range(data.shape[1]):
        if str(data.values[i,j])!='nan':
            temp.append(data.values[i,j])
    print(temp)
    transactions.append(temp)
from efficient_apriori import apriori
itemsets, rules = apriori(transactions, min_support=0.02,  min_confidence=0.5)#min_confidenceA到B的值
print("频繁项集：", itemsets)
print("关联规则：", rules)
#print(transactions)