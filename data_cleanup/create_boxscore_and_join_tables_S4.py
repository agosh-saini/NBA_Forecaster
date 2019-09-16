# -*- coding: utf-8 -*-
"""
Created on Sep 14 2019

@author: Agosh Saini (as7saini@edi.uwaterloo.ca)
"""
# This file creates boxscore in nba_games
# Also joins boxscore with betting files

import numpy as np
import pandas as pd

np.random.seed(8)


def create_boxscore(df):
    # drops NaN, resets index, and generates boxscore coloumn
    df = df.dropna()
    df = df.reset_index().drop('index', axis=1)
    df['boxscore'] = ['']*len(df)

    for i in range(len(df)-1):
        # creates boxscore value and adds to df
        date = df.loc[i, 'game_date']
        date = str(date).replace('-', '')
        team_id = df.loc[i, 'team_id']
        boxscore = date + '0' + team_id

        df.loc[i, 'boxscore'] = boxscore

    return df


def boxscore_merge(df1, df2):
    # merges boxscore to betting data
    df3 = df1.merge(df2, how='inner', on='game_id')
    return df3


team_id_data = pd.read_csv(r'modified_data/S3_team_id_replaced_data.csv',
                           skipinitialspace=True)

modified_odds_data = pd.read_csv(r'modified_data/S2_nba_betting_book.csv',
                                 skipinitialspace=True)

boxscore_replaced_data = create_boxscore(team_id_data)

finalized_data_bets = boxscore_merge(modified_odds_data,
                                     boxscore_replaced_data.loc[:, ['game_id', 'boxscore']])

finalized_data_bets.to_csv(r'modified_data/S4_finalized_data.csv', index=False)
