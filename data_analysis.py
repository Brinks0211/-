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


def expectancy(data):
    a = 100
    n = 0.25
    for i in data:
        if i == 'right':
            a = a + n*200
        if i == 'left':
            a = a - n*200
        if i == 'right' or i == 'left':
            n = n/2
    return a


def data_analysis(data_file):
    V = []
    f = pd.read_csv(data_file, encoding='utf-8', header=0, skip_blank_lines=True)
    f_use_time = f['rating.response']
    f_questionaire_score = f['question_key.keys']
    f_differ = abs(f['key_resp_sound_end.rt'] - f['emerge'])
    f_one_week = f['one_week_key.keys']
    f_one_month = f['one_month_key.keys']
    f_six_months = f['six_months_key.keys']
    questionaire_score = np.sum(f_questionaire_score)
    one_week = expectancy(f_one_week)
    one_month = expectancy(f_one_month)
    six_months = expectancy(f_six_months)
    V.append(one_week)
    V.append(one_month)
    V.append(six_months)
    aver = np.mean(f_differ)
    A = 200
    for index, i in enumerate(V):
        if index == 0:
            k_one_week = (i/A - 1) / 0.25
        elif index == 1:
            k_one_month = (i/A - 1) / 1
        elif index == 2:
            k_six_months = (i/A - 1) / 6
    k_list = [k_one_week, k_one_month, k_six_months]
    k_aver = np.mean(k_list)

    return f_use_time[0], round(questionaire_score, 0), round(aver, 4),\
           round(one_week, 2), round(one_month, 2), round(six_months, 2), \
           round(k_one_week, 2), round(k_one_month, 2), round(k_six_months, 2), round(k_aver, 2)


output_data = pd.DataFrame([], index=list(range(len(files))),
                           columns=['use_time', 'questionaire_score',
                                    'rt_difference', 'one_week', 'one_month',
                                    'six_months', 'k_one_week', 'k_one_month', 'k_six_months', 'k_aver', 'file'])
for index, i in enumerate(files):
    path_file = path+'\\'+i
    use_time, questionaire_score, aver, exp_one_week, exp_one_month, exp_six_months, \
    k_one_week, k_one_month, k_six_months, k_aver = data_analysis(path_file)
    output_data.loc[index, 'use_time'] = use_time
    output_data.loc[index, 'questionaire_score'] = questionaire_score
    output_data.loc[index, 'rt_difference'] = aver
    output_data.loc[index, 'one_week'] = exp_one_week
    output_data.loc[index, 'one_month'] = exp_one_month
    output_data.loc[index, 'six_months'] = exp_six_months
    output_data.loc[index, 'k_one_week'] = k_one_week
    output_data.loc[index, 'k_one_month'] = k_one_month
    output_data.loc[index, 'k_six_months'] = k_six_months
    output_data.loc[index, 'k_aver'] = k_aver
    output_data.loc[index, 'file'] = i
output_data.to_csv('output_data.csv', index=False)
