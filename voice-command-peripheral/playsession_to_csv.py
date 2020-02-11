import pandas as pd
from datetime import datetime, timedelta
import time

vcp_log_df = pd.read_csv('../data/logs/vcp_log.csv')
vcp_dt_df = vcp_log_df.copy()

vcp_dt_df['datetime'] = pd.to_datetime(vcp_dt_df['datetime'], format='%Y-%m-%d %H:%M:%S.%f')

def playsession_analysis(interval):
    playsession_list = []
    playsession_entry = {
        'session_start' : vcp_dt_df.loc[0, 'datetime'],
        'session_end' : vcp_dt_df.loc[0, 'datetime'],
        'session_seconds' : timedelta().total_seconds(),
        'sequence' : 1 if vcp_dt_df.loc[0, 'mode'] == 'sequence' else 0,
        'special' : 1 if vcp_dt_df.loc[0, 'mode'] == 'special' else 0,
        'incorrect' : 1 if vcp_dt_df.loc[0, 'mode'] == 'incorrect' else 0,
        'total_commands' : 1
    }

    last_row = len(vcp_dt_df)
    for i in range(1, last_row):
        if (vcp_dt_df.loc[i, 'datetime'] - vcp_dt_df.loc[i-1, 'datetime']).total_seconds() < interval:
            playsession_entry['session_end'] = vcp_dt_df.loc[i, 'datetime']
            playsession_entry[vcp_dt_df.loc[i, 'mode']] += 1
            playsession_entry['total_commands'] += 1
        else:
            playsession_entry['session_seconds'] = (playsession_entry['session_end'] - playsession_entry['session_start']).total_seconds()
            playsession_list.append(playsession_entry)

            playsession_entry = {
                'session_start' : vcp_dt_df.loc[i, 'datetime'],
                'session_end' : vcp_dt_df.loc[i, 'datetime'],
                'session_seconds' : timedelta().total_seconds(),
                'sequence' : 1 if vcp_dt_df.loc[i, 'mode'] == 'sequence' else 0,
                'special' : 1 if vcp_dt_df.loc[i, 'mode'] == 'special' else 0,
                'incorrect' : 1 if vcp_dt_df.loc[i, 'mode'] == 'incorrect' else 0,
                'total_commands' : 1
            }
    playsession_entry['session_seconds'] = (playsession_entry['session_end'] - playsession_entry['session_start']).total_seconds()
    playsession_list.append(playsession_entry)

    return pd.DataFrame(playsession_list)

while True:
    try:
        howmany_seconds = input('How many seconds long do you want your intervals? (Leave blank to exit) ')
        if howmany_seconds == '':
            break
        file_name = 'vcp_playsessions_' + howmany_seconds + 's_interval.csv'
        playsession_analysis(int(howmany_seconds)).to_csv('../data/playsessions/' + file_name)
        print(file_name + ' saved', '----------------------------------------------------------------', sep='\n')
    except ValueError:
        print('Please enter an integer or leave blank')