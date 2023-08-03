import datetime
from datetime import datetime
import pandas as pd

df = pd.read_csv('data/country_timeseries.csv', encoding='utf-8')

# pandas 에 있는 to_datetime() 날짜형식으로 변환
df['date_dt'] = pd.to_datetime(df['Date'], format='%Y/%m/%d') # 컬럼추가

print(df.head())
print(type(df.loc[0,'date_dt']))