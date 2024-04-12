import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Data\matches_use_3.xlsx")
data_2023 = data[data['Season_End_Year'] == 2023]

goal = {}

for i, row in data_2023.iterrows():
    home = row['Home']
    away = row['Away']
    homegoals = row['HomeGoals']
    awaygoals = row['AwayGoals']
    ftr = row['FTR']

    if home not in goal:
        goal[home] = {'match' : 0}
    if away not in goal:
        goal[away] = {'match' : 0}

    if ftr == 'H':
        if awaygoals == 0:
            goal[home]['match'] += 1
    elif ftr == 'A':
        if homegoals == 0:
            goal[away]['match'] += 1
    else:
        if homegoals == 0 and awaygoals == 0:
            goal[home]['match'] += 1
            goal[away]['match'] += 1

# file = pd.DataFrame.from_dict(goal, orient='index')
# file.columns = ['Match']
# file['Club'] = file.index
# file = file[['Club', 'Match']]
# file.to_excel('Python\Question 8\Match 2023.xlsx', index=False)

# Draw Map
data_map = pd.read_excel('Python\Question 8\Match 2023.xlsx')

check_data = data_map[data_map['Match'] > 11]

check_data.set_index('Club', inplace=True)
check_data['Match'].plot.area(figsize=(10,5))

plt.xlabel('Club')
plt.ylabel('Score')
plt.title('Score for Matchest')
plt.xticks(rotation=0)
plt.show()