# -*- coding: utf-8 -*-
'''
Created on Aug 28 2019

@author: Agosh Saini (as7saini@edu.uwaterloo.ca)

paper this file is based on: 
https://library.ndsu.edu/ir/bitstream/handle/10365/28084/Predicting%20Outcomes%20of%20NBA%20Basketball%20Games.pdf

Stats from:
https://www.basketball-reference.com
'''

import numpy as np
import pandas as pd

from datetime import datetime
from sportsreference.nba.boxscore import Boxscores

'''Functions'''
def pull_year_data(start, end):
    games = Boxscores(start, end).games
    coloumns = ['boxscore', 'away_name', 'away_abbr', 
                'away_score', 'home_name', 'home_abbr', 'home_score', 'winning_name',
                'winning_abbr', 'losing_name', 'losing_abbr']
    df = pd.DataFrame( columns=coloumns)

    for key in games.items():
        day = key[1]
        for i in range(len(day)-1):
            df = df.append(day[i], ignore_index=True)
    return df

'''Gettting All Data'''
import time

win_loss_16_17 = pull_year_data(datetime(2016, 10, 25), datetime(2017, 6, 18))
win_loss_16_17.to_csv(r'sportsreference_data\2016_17_games.csv')
print('sleeping for 1 sec ...')
time.sleep(1)

win_loss_17_18 = pull_year_data(datetime(2017, 10, 17), datetime(2018, 6, 17))
win_loss_17_18.to_csv(r'sportsreference_data\2017_18_games.csv')
print('sleeping for 1 sec ...')
time.sleep(1)

win_loss_18_19 = pull_year_data(datetime(2018, 10, 1), datetime(2019, 6, 30))
win_loss_18_19.to_csv(r'sportsreference_data\2018_19_games.csv')




    



    