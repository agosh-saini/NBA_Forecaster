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

def game_diff_data(dataset_team_stats, dataset_games, abrs):
    coloumns = {'PER': [], 'TS%': [], '3PAr': [], 'FTr': [], 'ORB%': [], 'AST%': [], 'TOV%': [], 'PT': []}
    df = pd.DataFrame(coloumns)
    
    for i in range(len(dataset_games)-1):
        visit, home, pts_v, pts_h = dataset_games['Visitor'].values[i], dataset_games['Home'].values[i], dataset_games['PTS-V'].values[i], dataset_games['PTS-H'].values[i] 
        
        dataset_v = dataset_team_stats[dataset_team_stats['Team'].values == visit]
        dataset_h = dataset_team_stats[dataset_team_stats['Team'].values == home]
        
        per, ts, threePar = dataset_v['PER'].values-dataset_h['PER'].values, dataset_v['TS%'].values-dataset_h['TS%'].values, dataset_v['3PAr'].values-dataset_h['3PAr'].values
        ftr, orb, ast, tov = dataset_v['FTr'].values-dataset_h['FTr'].values, dataset_v['ORB%'].values-dataset_h['ORB%'].values, dataset_v['AST%'].values-dataset_h['AST%'].values, dataset_v['TOV%'].values-dataset_h['TOV%'].values
        
        pt = pts_v - pts_h
        
        
        data = {'PER': per, 'TS%': ts, '3PAr': threePar, 'FTr': ftr, 'ORB%': orb, 'AST%': ast, 'TOV%': tov, 'PT': pt}
        
        if np.size(per) == 0 or np.size(ts) == 0 or np.size(threePar) == 0 or np.size(pt) == 0 or np.size(ftr) == 0 or np.size(orb) == 0 or np.size(ast) == 0 or np.size(tov) == 0:
            continue
        
        df = df.append(data, ignore_index=True)
        
    return df
        

#Getting All Datasets
abrs_team = pd.read_csv(r'Stats\abrs_team.csv', skipinitialspace=True)
name, abr = abrs_team['Team'].values, abrs_team['abrs'].values

#2016-17 Season Data Pre-Processing
dataset_2016_17 = pd.read_csv(r'Stats\2016-17.csv', skipinitialspace=True)
wins_2016_17 = pd.read_csv(r'Stats\wins_2016-17.csv', skipinitialspace=True)
games_2016_17 = pd.read_csv(r'Stats\2016-17_games.csv', skipinitialspace=True)

y2016_17 = clean_data(dataset_2016_17, 5)
      
tm_stats_16_17 = tm_stats(y2016_17, abr, name, wins_2016_17).dropna()

game_data_16_17 = game_diff_data(tm_stats_16_17, games_2016_17, abr).dropna()

#2017-18 Season Data Pre-Proce
dataset_2017_18 = pd.read_csv(r'Stats\2017-18.csv', skipinitialspace=True)
wins_2017_18 = pd.read_csv(r'Stats\wins_2017-18.csv', skipinitialspace=True)
games_2017_18 = pd.read_csv(r'Stats\2017-18_games.csv', skipinitialspace=True)

y2017_18 = clean_data(dataset_2017_18, 5)
      
tm_stats_17_18 = tm_stats(y2017_18, abr, name, wins_2017_18).dropna()

game_data_17_18 = game_diff_data(tm_stats_17_18, games_2017_18, abr).dropna()

#2018-19 Season Data Pre-Processing
dataset_2018_19 = pd.read_csv(r'Stats\2018-19.csv', skipinitialspace=True)
wins_2018_19 = pd.read_csv(r'Stats\wins_2018-19.csv', skipinitialspace=True)
games_2018_19 = pd.read_csv(r'Stats\2018-19_games.csv', skipinitialspace=True)

y2018_19 = clean_data(dataset_2018_19, 5)
      
tm_stats_18_19 = tm_stats(y2018_19, abr, name, wins_2018_19).dropna()

game_data_18_19 = game_diff_data(tm_stats_18_19, games_2018_19, abr).dropna()

#Combining all game_data_[YEAR] datasets
three_year_game_data = pd.concat([game_data_16_17, game_data_17_18, game_data_18_19]).dropna()

