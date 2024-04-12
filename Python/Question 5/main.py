import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data\matches_use_3.xlsx")

streaks = {}

write = pd.DataFrame(columns=['Season','Club','Max Streaks'])

for season in data['Season_End_Year'].unique():
    season_data = data[data['Season_End_Year'] == season]
    streaks = {team:{'max':0, 'current':0} for team in pd.concat([season_data['Home'], season_data['Away']]).unique()}

    for ind, row in season_data.iterrows():
        home_team = row['Home']
        away_team = row['Away']
        result = row['FTR']

        if result == 'H':
            streaks[home_team]['current'] += 1
            streaks[home_team]['max'] = max(streaks[home_team]['max'], streaks[home_team]['current'])
            streaks[away_team]['current'] = 0
        elif result == 'A':
            streaks[away_team]['current'] += 1
            streaks[away_team]['max'] = max(streaks[away_team]['max'], streaks[away_team]['current'])
            streaks[home_team]['current'] = 0
        else:
            streaks[home_team]['current'] += 1
            streaks[away_team]['current'] += 1

    max_streaks_team = max(streaks, key=lambda team:streaks[team]['max'])
    max_streaks = streaks[max_streaks_team]['max']

    new_row = pd.DataFrame({'Season': [season], 'Club': [max_streaks_team], 'Max Streaks': [max_streaks]})
    write = pd.concat([write, new_row], ignore_index=True)

# write.to_csv('Data\streaks_2.csv', index=False)

# Draw Map

data_map = pd.read_excel('Python\Question 5\streaks_2.xlsx')

max_streaks = {}

for i, row in data_map.iterrows():
    team = row['Club']
    streaks = row['Max Streaks']

    if team not in max_streaks or streaks > max_streaks[team]:
        max_streaks[team] = streaks


plt.figure(figsize=(40, 10))
plt.bar(max_streaks.keys(), max_streaks.values())
plt.xlabel('Club')
plt.ylabel('Max Streaks')
plt.title('Max Streaks by Club')
plt.xticks(rotation=0)
plt.show()