import pandas as pd

df = pd.read_csv('datago/201212_201412_연령별인구현황_연간.csv', encoding='cp949')

print(df.iloc[1,0])
print(df.iloc[1,6])
print(df.iloc[1,34])
