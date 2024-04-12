import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Data\matches_use_3.xlsx")

seasons = [2019,2020,2021,2022,2023]
liverpoolfc = {season : {'goals' : 0, 'points' : 0} for season in seasons}

for i, row in data.iterrows():
    if row['Season_End_Year'] in seasons:
        if row['Home'] == 'Liverpool':
            liverpoolfc[row['Season_End_Year']]['goals'] += row['HomeGoals']
            if row['FTR'] == 'H':
                liverpoolfc[row['Season_End_Year']]['points'] += 3
            elif row['FTR'] == 'D':
                liverpoolfc[row['Season_End_Year']]['points'] += 1
        elif row['Away'] == 'Liverpool':
            liverpoolfc[row['Season_End_Year']]['goals'] += row['AwayGoals']
            if row['FTR'] == 'A':
                liverpoolfc[row['Season_End_Year']]['points'] += 3
            elif row['FTR'] == 'D':
                liverpoolfc[row['Season_End_Year']]['points'] += 1

matches = 38

for season in liverpoolfc:
    liverpoolfc[season]['goals_per'] = liverpoolfc[season]['goals'] / matches
    liverpoolfc[season]['point_per'] = liverpoolfc[season]['points'] / matches

file = pd.DataFrame(liverpoolfc).T
file.reset_index(inplace=True)
file.columns = ['Season', 'Goals', 'Point','Goal Performance', 'Point Performance']
# file.to_excel('Python\Question 9\Liverpool.xlsx')

# Draw Map

plt.plot(file['Goal Performance'], label='Goal Performance')
plt.plot(file['Point Performance'], label='Point Performance')
plt.xlabel('Goals')
plt.ylabel('Points')
plt.title('Liverpool FC')
plt.legend()
plt.show()