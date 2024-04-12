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
            teams[row['Home']] = {'points' : 0, 'goals' : 0, 'win' : 0, 'draw' : 0, 'lose' : 0}
        if row['Away'] not in teams:
            teams[row['Away']] = {'points' : 0, 'goals' : 0, 'win' : 0, 'draw' : 0, 'lose' : 0}

        if row['FTR'] == 'H':
            teams[row['Home']]['points'] += 3
            teams[row['Home']]['win'] += 1
            teams[row['Away']]['lose'] += 1
            teams[row['Home']]['goals'] += row['HomeGoals']
            teams[row['Away']]['goals'] += row['AwayGoals']
            
        elif row['FTR'] == 'A':
            teams[row['Away']]['points'] += 3
            teams[row['Home']]['lose'] += 1
            teams[row['Away']]['win'] += 1
            teams[row['Home']]['goals'] += row['HomeGoals']
            teams[row['Away']]['goals'] += row['AwayGoals']
        else:
            teams[row['Home']]['points'] += 1
            teams[row['Away']]['points'] += 1
            teams[row['Home']]['draw'] += 1
            teams[row['Away']]['draw'] += 1
            teams[row['Home']]['goals'] += row['HomeGoals']
            teams[row['Away']]['goals'] += row['AwayGoals']
    for team, data in teams.items():
        results_charts.append({f'Season' : season, 'Team' : team, 'Points' : data['points'], 'Goals' : data['goals']})

    max_point = max(teams.items(), key=lambda x: x[1]['points'])
    champions[season] = max_point[0]

    results_champion.append({
        'Season' : season,
        'Champion' : max_point[0],
        'Points' : max_point[1]['points'],
        'Win' : max_point[1]['win'],
        'Draw' : max_point[1]['draw'],
        'Lose' : max_point[1]['lose']
    })

# results_write_charts = pd.DataFrame(results_charts)
# results_write_charts.to_csv('Data\charts.csv', index=False)

# results_write_champion = pd.DataFrame(results_champion)
# results_write_champion.to_csv('Data\champion.csv', index=False)

# Draw Map

data_map = pd.read_excel('Python\Question 3\champion.xlsx')

check = data_map[data_map['Lose'] == 0]

label = ['Win', 'Draw', 'Lose']
size = [check['Win'].values[0],check['Draw'].values[0],check['Lose'].values[0]]
colors = ['green', 'silver', 'red']

fig1, ax1 = plt.subplots()
ax1.pie(size, labels=label, colors=colors, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.title('Match Results Arsenal')
plt.show()