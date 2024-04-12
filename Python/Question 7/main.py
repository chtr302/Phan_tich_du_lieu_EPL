import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel("Data\matches_use_3.xlsx")

data_2023 = data[data['Season_End_Year'] == 2023]
win_match = {}

for i, row in data_2023.iterrows():
    home = row['Home']
    away = row['Away']
    ftr = row['FTR']

    if home not in win_match:
        win_match[home] = {'win' : 0}
    if away not in win_match:
        win_match[away] = {'win' : 0}

    if ftr == 'H':
        win_match[home]['win'] += 1
    elif ftr == 'A':
        win_match[away]['win'] += 1

total_matchs = 38

for team in win_match:
    win_match[team]['av_win'] = win_match[team]['win'] / total_matchs

# file = pd.DataFrame.from_dict(win_match, orient='index')
# file.columns = ['Win Match', 'Average Win Match']
# file['Club'] = file.index
# file = file[['Club', 'Win Match', 'Average Win Match']]
# file.to_excel('Python\Question 7\Win Match 2023.xlsx', index=False)

# Draw Map

data_map = pd.read_excel('Python\Question 7\Win Match 2023.xlsx')

teams = ['Liverpool', 'Tottenham', 'Chelsea', 'Manchester Utd', 'Arsenal', 'Manchester City']

data_map = data_map[data_map['Club'].isin(teams)]
data_map.set_index('Club', inplace=True)

draw = data_map['Average Win Match']
draw.plot(kind='pie', autopct='%1.1f%%')

plt.title('Average Win Match')
plt.ylabel('Club')
plt.show()