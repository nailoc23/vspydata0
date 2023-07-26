import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        'aaaa': [10,20],
        'bbbb': [10,30],
        'cccc': [10,50]
    }
)
# 컬럼명변경 rename
#df.index = ['A', 'B']
df.columns = ['한국','중국','일본']
print(df)
#print(df.loc['A'])
print(df.iloc[0])