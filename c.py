import pandas as pd
import os
import subprocess
import time
import re

df = pd.read_csv('change_250.csv')
prev_score = 0.8302
for i in range(250, 301):
    df.loc[i, 'Transported'] = not df.loc[i, 'Transported']
    print(f'changed to {df.loc[i, "Transported"]} ')
    df.to_csv(f'change_{i}.csv', index=False)
    time.sleep(15)
    os.system(f'kaggle competitions submit -c koitest1 -f change_{i}.csv -m "Message"')
    time.sleep(15)
    res = subprocess.run(['kaggle', 'competitions', 'submissions', '-c', 'koitest1'],
                         stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(res)
    score = float(res.split('\n')[3].split('complete  ')[1].split('  ')[0].strip())
    print(i, score)
    if score > prev_score:
        prev_score = score
    else:
        df.loc[i, 'Transported'] =not df.loc[i, 'Transported']
        print(f'reverted to {df.loc[i, "Transported"]} ')