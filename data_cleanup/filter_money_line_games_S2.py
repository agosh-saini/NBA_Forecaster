# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 23:36:37 2019

@author: Agosh Saini (as7saini@edi.uwaterloo.ca)
"""

#Cleans up data
#filters only for Pinnacle Sports website odds

import numpy as np
import pandas as pd

np.random.seed(8)

#Looks for Pinnacle Sports in the book_name coloumn and sorts out everything else
def clean_up_bets(df, name):
    df = df[df['book_name']==name]
    return df

bet_data = pd.read_csv(r'sources/nba_betting_money_line.csv', skipinitialspace=True)

bet_data = clean_up_bets(bet_data, 'Pinnacle Sports')

bet_data.to_csv(r'modified_data/S2_nba_betting_book.csv')