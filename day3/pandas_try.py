import random
import pandas as pd

df = pd.read_csv('engine_log.csv', delimiter=',')

print(df)
# print('test')

# ubah value dari sell kedua pada column temperatures
df.loc[1, 'Temperatures'] = 85.55

for i in range(10):
    # tambah baris baru
    temp = round(random.uniform(71, 86), 2)
    press = round(random.uniform(9.5, 11.6), 2)

    num = len(df) + 1
    df.loc[len(df)] = [num, temp, press]


df.to_csv('engine_log.csv', index=False, sep=',')