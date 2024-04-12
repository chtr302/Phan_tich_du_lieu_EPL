import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Data\matches_use_3.xlsx")

data_2023 = data[data['Season_End_Year'] == 2023]
streaks = {}

for i,row in data_2023.iterrows():
    home = row['Home']
    away = row['Away']
    ftr = row['FTR']
    home_goals = row['HomeGoals']
    away_goals = row['AwayGoals']

    if home not in streaks:
        streaks[home] = {'win' : 0, 'lose' : 0}
    if away not in streaks:
        streaks[away] = {'win' : 0, 'lose' : 0}

    if ftr == 'H':
        streaks[home]['win'] += home_goals
        streaks[away]['lose'] += away_goals
    elif ftr == 'A':
        streaks[home]['lose'] += home_goals
        streaks[away]['win'] += away_goals
    else:
        streaks[home]['win'] += home_goals
        streaks[home]['lose'] += home_goals
        streaks[away]['win'] += away_goals
        streaks[away]['lose'] += away_goals

total_matchs = 38

for team in streaks:
    streaks[team]['avg_win'] = streaks[team]['win'] / total_matchs
    streaks[team]['avg_lose'] = streaks[team]['lose'] / total_matchs

# streaks_df = pd.DataFrame.from_dict(streaks, orient='index')
# streaks_df.columns = ['Win Score','Lose Score', 'Average Win', 'Average Lose']
# streaks_df['Club'] = streaks_df.index
# streaks_df = streaks_df[['Club', 'Win Score', 'Lose Score', 'Average Win', 'Average Lose']]
# streaks_df.to_excel('Python\Question 6\streaks_2023.xlsx', index=False)

# Draw Map

data_map = pd.read_excel('Python\Question 6\streaks_2023.xlsx')

teams = ['Liverpool', 'Tottenham', 'Chelsea', 'Manchester Utd', 'Arsenal', 'Manchester City']

data_map = data_map[data_map['Club'].isin(teams)]

draw = data_map[['Club', 'Average Win', 'Average Lose']].set_index('Club')
draw.plot(kind='bar', stacked=False)

plt.title('Average Win and Lose Scores')
plt.xlabel('Club')
plt.ylabel('Average Score')
plt.xticks(rotation=0)
plt.show()