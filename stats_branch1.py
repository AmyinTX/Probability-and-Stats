# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 10:23:27 2017

@author: amybrown
"""
""" Unit 2, Lesson 1, Assignment 1 Challenge """
import pandas as pd
from scipy import stats # will need this package for obtaining mode later

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data=data.splitlines()

data = [i.split(',') for i in data] # splits items in each list on commas

column_names = data[0] # for first row-identifies the field headers
data_rows = data[1::] # identifies the data rows
df = pd.DataFrame(data_rows, columns=column_names) # converts to pandas dataframe

df['Alcohol'] = df['Alcohol'].astype(float) # converts dataframe item to float
df['Tobacco'] = df['Tobacco'].astype(float)

mean_alc = df['Alcohol'].mean()
med_alc = df['Alcohol'].median()
mode_alc = stats.mode(df['Alcohol']) # mode returns the smallest number when there is not any numbers that occur mt once
range_alc = max(df['Alcohol']) - min(df['Alcohol']) #obtains range
std_alc = df['Alcohol'].std() #obtains standard deviation
var_alc = df['Alcohol'].var()   # obtains variance

mean_tob = df['Tobacco'].mean()
med_tob = df['Tobacco'].median()
mode_tob = stats.mode(df['Tobacco'])
range_tob = max(df['Tobacco']) - min(df['Tobacco']) #obtains range
std_tob = df['Tobacco'].std() #obtains standard deviation
var_tob = df['Tobacco'].var()

alc_dict = {'alcohol': {'mean': mean_alc, 'median': med_alc, 'mode': mode_alc, 'range': range_alc, 'std': std_alc, 'var': var_alc}}
tob_dict = {'tobacco': {'mean': mean_tob, 'med': med_tob, 'mode': mode_tob, 'range': range_tob, 'std': std_tob, 'var': var_tob}}

dfname='Alcohol and Tobacco dataset'

for v in alc_dict.values():
    print(v)
