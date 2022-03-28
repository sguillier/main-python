import pandas as pd
import numpy as np

df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, np.nan],
                   [np.nan, 3, np.nan, 4]],
                  columns=list("ABCD"))

for row in df.iterrows():
    print(row[1]['A'], row[1]['B'], row[1]['C'], row[1]['D'])


df.fillna(0, inplace=True)

for row in df.iterrows():
    print(row[1]['A'], row[1]['B'], row[1]['C'], row[1]['D'])

df2 = pd.DataFrame([[]])

df2.fillna(0, inplace=True)

for row in df2.iterrows():
    print(row[1]['A'], row[1]['B'], row[1]['C'], row[1]['D'])