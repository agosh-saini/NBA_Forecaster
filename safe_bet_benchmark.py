import pandas as pd
import numpy as np

game_info_df = pd.read_csv(
    'sportsreference_data/2016_17_games.csv', index_col=0)
betting_info_df = pd.read_csv('sportsreference_data/final_moneyline_data.csv')

# merging betting odds info with win/loss info
game_data_with_odds_df = game_info_df.loc[:, ['boxscore', 'home_abbr', 'away_abbr', 'winning_abbr']].merge(
    betting_info_df.loc[:, ['boxscore', 'home_odds', 'away_odds']],
    on='boxscore')


# Initializing an array to keep track of net profits for safe bets
profit_arr = []

# investment in each match
investment = 50

# variable to keep track of total investment made
total_investment = 0

# Going to iterate thorugh each row of dataframe to find out net profit on safe bets
for index, row in list(game_data_with_odds_df.iterrows()):
    bet_return = investment
    # Case where home team is the safer bet
    if row['home_odds'] <= row['away_odds']:
        # Case where favoured home team wins
        if row['home_abbr'] == row['winning_abbr']:
            # Subtracting to return net profit instead of net revenue
            bet_return *= row['home_odds'] - 1
        # Case where favoured team loses. Safe bet loses money
        else:
            bet_return *= -1
    # Case where away team is the safer bet
    if row['away_odds'] < row['home_odds']:
        # Case where favoured away team wins
        if row['away_abbr'] == row['winning_abbr']:
            # Subtracting to return net profit instead of net revenue
            bet_return *= row['away_odds'] - 1
        # Case where favoured team loses. Safe bet loses money
        else:
            bet_return *= -1
    profit_arr.append(bet_return)
    total_investment += investment

game_data_with_odds_df['safe_net_profit'] = profit_arr

game_data_with_odds_df.to_csv('Analysis/safe_bet_analysis.csv')

# Split profits into batches of 25 matches(roughly the number of matches each week)
batch_profits = []
cutoff = 25
index = 0
while index < len(profit_arr):
    batch = 0
    while index < cutoff:
        print(index, cutoff)
        batch += profit_arr[index]
        index += 1
    batch_profits.append(batch)
    if cutoff < len(profit_arr) - 25:
        cutoff += 25
    else:
        break
