# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 14:28:37 2017

@author: wew647

Take the SSNAP data that is in a complex format (multicolumn headers/multiyears) and extract only the necessary data types in the latest year
"""

import pandas as pd


ssnap = pd.read_excel('SSNAP_1516_CCG.xlsx', sheetname=1, index_col=1)

##want latest year only
year1516Cols=ssnap.iloc[:1]=='Apr 2015-Mar 2016'


#Turn into a series to use as boolean mask
rightYear=pd.Series(year1516Cols.iloc[0])

#Only want AF and Medication related rows
rowIndices=['Item Reference','F6.1','F6.12', 'F6.19','F6.21','F6.23','F6.25']
cutdown=ssnap.loc[rowIndices,rightYear]

#Add more useful labels
cutdown.insert(0,'labels',['CCG','Atrial Fibrillation (AF) before stroke', 'If AF before stroke, on anticoagulant medication:', 'Both anticoagulant and antiplatelet medication','Anticoagulant medication only','Antiplatelet medication only','Neither medication'])

#Finally, have CCGs row wise to merge w QOF data! 
cutdownT=cutdown.transpose()