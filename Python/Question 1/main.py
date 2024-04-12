import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Data\matches_use_3.xlsx")

seasons = data.groupby('Season_End_Year')
results_charts = []
champions = {}
results_champion = []

for season, season_data in seasons:
    teams = {}
    for colum, row in season_data.iterrows():
        if row['Home'] not in teams:
            teams[row['Home']] = {'points' : 0, 'goals' : 0}
        if row['Away'] not in teams:
            teams[row['Away']] = {'points' : 0, 'goals' : 0}

        if row['FTR'] == 'H':
            teams[row['Home']]['points'] += 3
            teams[row['Home']]['goals'] += row['HomeGoals']
            teams[row['Away']]['goals'] += row['AwayGoals']
        elif row['FTR'] == 'A':
            teams[row['Away']]['points'] += 3
            teams[row['Home']]['goals'] += row['HomeGoals']
            teams[row['Away']]['goals'] += row['AwayGoals']
        else:
            teams[row['Home']]['points'] += 1
            teams[row['Away']]['points'] += 1
            teams[row['Home']]['goals'] += row['HomeGoals']
            teams[row['Away']]['goals'] += row['AwayGoals']
    for team, data in teams.items():
        results_charts.append({f'Season' : season, 'Team' : team, 'Points' : data['points'], 'Goals' : data['goals']})

    max_point = max(teams.items(), key = lambda x: x[1]['points'])
    champions[season] = max_point[0]

# for season, champion in champions.items():
#     results_champion.append({'Season' : season, 'Champion' : champion})

# results_write_charts = pd.DataFrame(results_charts)
# results_write_charts.to_excel('Data\charts.xlsx', index=False)

# results_write_champion = pd.DataFrame(results_champion)
# results_write_champion.to_csv('Python\Question 1\champion.csv', index=False)

# Draw Map

champions_map = pd.read_csv("Python\Question 1\champion.csv")
champion_counts = champions_map['Champion'].value_counts()

plt.figure(figsize=(10,6))
champion_counts.plot(kind='bar')
plt.title('Number of Championships per Team')
plt.xlabel('Team')
plt.ylabel('Number of Championships')
plt.xticks(rotation=0)
plt.show()
