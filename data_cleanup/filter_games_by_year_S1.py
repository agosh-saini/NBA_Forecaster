# -*- coding: utf-8 -*-
"""
Created on Sun Sept 12, 2019

@author: as7saini@edu.uwaterloo.ca

dataset from: 
https://www.kaggle.com/ehallmar/nba-historical-stats-and-betting-data/downloads/nba-historical-stats-and-betting-data.zip/1
"""

#THIS FILE CLEANS UP THE DATA
#It fitlers out year data from the seasons 2016, 2017, 2018

import numpy as np
import pandas as pd

np.random.seed(8)

#cleans up the csv file by filtering for only the years 
#we want the games from
def clean_year(df, years):
    df = df[df['season_year'].isin(years)]
    return df

game_data = pd.read_csv(r'sources/nba_games_all.csv', skipinitialspace=True)

game_data = clean_year(game_data, [2016, 2017, 2018])

game_data.to_csv(r'modified_data/S1_nba_games_all.csv')
