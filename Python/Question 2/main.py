import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Python\Question 2\champion.xlsx")

current_champion = None
current_point = 0
streaks = {}

for season, champion in data.iterrows():
    if champion['Champion'] == current_champion:
        current_point += 1
    else:
        if current_champion is not None and current_point > streaks.get(current_champion,0):
            streaks[current_champion] = current_point
        current_champion = champion['Champion']
        current_point = 1

if current_champion is not None and current_point > streaks.get(current_champion,0):
    streaks[current_champion] = current_point

sorted_streaks = dict(sorted(streaks.items(),key=lambda item:item[1], reverse=True))

clb = list(sorted_streaks.keys())
point = list(sorted_streaks.values())

plt.figure(figsize=(10, 5))
plt.plot(clb, point, marker = 'o')
plt.xlabel('Champion Club')
plt.ylabel('Championships Point')
plt.title('Championships by Club')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()
