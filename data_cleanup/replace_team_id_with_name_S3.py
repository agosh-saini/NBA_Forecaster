# -*- coding: utf-8 -*-
"""
Created on Sep 13 2019

@author: Agosh Saini (as7saini@edi.uwaterloo.ca)
"""
#This file replaces team ID in games file with team abreviation
#This file also gets rid of any non home games

import numpy as np
import pandas as pd

np.random.seed(8)

def replace_id_with_abrs(df, teams):
    #the is_home games are sorted in this line
    df = df[df['is_home']=='t']
    #setting variables
    team_ID, team_abr = teams['team_id'], teams['abbreviation']
    #replaces the team_ID with team_abr
    for i in range(len(teams)-1):
        df = df.replace(team_ID[i], team_abr[i])
    return df

modified_game_data = pd.read_csv(r'modified_data/S1_nba_games_all.csv', skipinitialspace=True)

team_data = pd.read_csv(r'sources/nba_teams_all.csv', skipinitialspace=True)

team_id_replaced_data = replace_id_with_abrs(modified_game_data, team_data)

team_id_replaced_data.to_csv(r'modified_data/S3_team_id_replaced_data.csv', index = False)