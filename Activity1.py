import pandas as pd

#PART ! - Create a Panda Series of top player scores
print('--- PART 1: Pandas Series ---')
scores = [98500, 87200, 76400, 65100, 54800]
players = pd.Series(scores, index=['NightWolf', 'StarBlaze', 'PixerlKnight', 'CyberFox', 'IronStorm'])
print(players)

#PART 2 - Create a DataFrame of gaming stats
print()
print('--- PART 2: Pandas DataFrame ---')
data = {
    'Player': ['Nightwolf', 'StarBlaze', 'PixelKnight', 'CyberFox', 'IronStorm'],
    'Level' :  [42, 38, 35, 27, 67],
    'Score' :  [98500, 87200, 76400, 65100, 54800],
    'Wins'  :   [210, 185, 162, 140, 118]
}
df = pd.DataFrame(data)
print(df)

#PART 3 - Access rows using .loc
print()
print('--- PART 3: Accessing Rows ---')
print('Rows 0 (top players):')
print(df.loc[0])
print()
print('Rows 2 and 3:')
print(df.loc[2:3])

