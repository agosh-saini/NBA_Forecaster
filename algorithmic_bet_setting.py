# -*- coding: utf-8 -*-
'''
Created on Sun Aug 18 19:57:37 2019

@author: Agosh Saini (as7saini@edu.uwaterloo.ca)

paper this file is based on: 
https://library.ndsu.edu/ir/bitstream/handle/10365/28084/Predicting%20Outcomes%20of%20NBA%20Basketball%20Games.pdf

Stats from:
https://www.basketball-reference.com
'''

#Imporiting Dependecies
import numpy as np
import pandas as pd

np.random.seed(8)

#Data Pre-Processing Fuctions
def clean_data(dataset, min_minutes): 
    #Cuts down on useless players
    drop_set = np.array([], dtype=int)
    for i in range(len(dataset.values)):
        if int(dataset['MP'].values[i])/int(dataset['G'].values[i]) > min_minutes:
            np.append(drop_set, i)
    
    dataset = dataset.drop(['Pos', 'Age', 'G', 'MP', 'DRB%', 
                            'TRB%', 'STL%', 'BLK%', 'USG%', 'DWS',
                            'WS', 'WS/48', 'OBPM', 'DBPM', 'VORP', 'BPM', 'OWS'], axis=1)
        
    return dataset.drop(drop_set, axis=0)

def tm_stats(dataset, abrs, name, wins):
    coloumns = {'Team': [], 'PER': [], 'TS%': [], '3PAr': [], 'FTr': [], 'ORB%': [], 'AST%': [], 'TOV%': [], 'W': []}
    df = pd.DataFrame(coloumns)
    for i in range(len(abrs)-1):
        dataset1 = dataset[dataset['Tm'].values == abrs[i]]
        wins1 = wins[wins['Team'] == name[i]]
        
        per, ts, threePar, win = np.mean(dataset1['PER'].values), np.mean(dataset1['TS%'].values), np.mean(dataset1['3PAr'].values), wins1['W'].values
        ftr, orb, ast, tov =  np.mean(dataset1['FTr'].values), np.mean(dataset1['ORB%'].values), np.mean(dataset1['AST%'].values), np.mean(dataset1['TOV%'].values)
        data = {'Team': abrs[i], 'PER': per, 'TS%': ts, '3PAr': threePar, 'FTr': ftr, 'ORB%': orb, 'AST%': ast, 'TOV%': tov, 'W': win}
        
        if np.size(per) == 0 or np.size(ts) == 0 or np.size(threePar) == 0 or np.size(win) == 0 or np.size(ftr) == 0 or np.size(orb) == 0 or np.size(ast) == 0 or np.size(tov) == 0:
            continue
        
        df = df.append(data, ignore_index=True)
        
    return df


#Getting All Datasets
abrs_team = pd.read_csv(r'Stats\abrs_team.csv', skipinitialspace=True)
name, abr = abrs_team['Team'].values, abrs_team['abrs'].values

#2016-17 Season Data Pre-Processing
dataset_2016_17 = pd.read_csv(r'Stats\2016-17.csv', skipinitialspace=True)
wins_2016_17 = pd.read_csv(r'Stats\wins_2016-17.csv', skipinitialspace=True)

y2016_17 = clean_data(dataset_2016_17, 10)
      
tm_stats_16_17 = tm_stats(y2016_17, abr, name, wins_2016_17)

#2017-18 Season Data Pre-Proce
dataset_2017_18 = pd.read_csv(r'Stats\2017-18.csv', skipinitialspace=True)
wins_2017_18 = pd.read_csv(r'Stats\wins_2017-18.csv', skipinitialspace=True)

y2017_18 = clean_data(dataset_2017_18, 10)
      
tm_stats_17_18 = tm_stats(y2017_18, abr, name, wins_2017_18)

#2018-19 Season Data Pre-Processing
dataset_2018_19 = pd.read_csv(r'Stats\2018-19.csv', skipinitialspace=True)
wins_2018_19 = pd.read_csv(r'Stats\wins_2018-19.csv', skipinitialspace=True)

y2018_19 = clean_data(dataset_2018_19, 10)
      
tm_stats_18_19 = tm_stats(y2018_19, abr, name, wins_2018_19)

#Joining All Pandas Dataframes
three_year_team_data = pd.concat([tm_stats_16_17, tm_stats_17_18, tm_stats_18_19])
three_year_team_data = three_year_team_data.dropna()

'''
Multiple Linear Regressin
In the paper they assume/prove it was linear hence I will go with that assumpyion 
'''

from sklearn import linear_model
from sklearn.model_selection import train_test_split

X = three_year_team_data[['PER', 'TS%', '3PAr', 'FTr', 'ORB%', 'AST%', 'TOV%']]
y = three_year_team_data['W']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

regr = linear_model.LinearRegression()

model = regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)

import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel('True Values')
plt.ylabel('Predictions')

print('Model Score: ', model.score(X_test, y_test))

from sklearn.metrics import mean_squared_error
from math import sqrt

print('RMSE: ', sqrt(mean_squared_error(y_test, y_pred)))

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)


