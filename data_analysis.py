import os
import pandas as pd
import numpy as np
path = os.getcwd()
path = path+'\\data'
dir_files = os.listdir(path)
files = []
for i in dir_files:
    if '.csv' in i:
        files.append(i)


def data_analysis(data_file):
    f = pd.read_csv(data_file, encoding='utf-8', header=0, skip_blank_lines=True)
    f_use_time = f['rating.response']
    f_differ = abs(f['key_resp_sound_end.rt'] - f['emerge'])
    f_direction = f['delay_discount_key.keys']
    aver = np.mean(f_differ)
    a = 100
    n = 0.25
    for i in f_direction:
        if i == 'right':
            a = a + n*a
        if i == 'left':
            a = a - n*a
        if i == 'right' or i == 'left':
            n = n/2
    return f_use_time[0], round(aver, 4), round(a, 2)


output_data = pd.DataFrame([], index=list(range(len(files))), columns=['use_time', 'rt_difference', 'expectancy', 'file'])
for index, i in enumerate(files):
    path_file = path+'\\'+i
    use_time, aver, exp = data_analysis(path_file)
    output_data.loc[index, 'use_time'] = use_time
    output_data.loc[index, 'rt_difference'] = aver
    output_data.loc[index, 'expectancy'] = exp
    output_data.loc[index, 'file'] = i
output_data.to_csv('output_data.csv')
