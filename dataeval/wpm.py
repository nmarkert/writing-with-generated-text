import pandas as pd
from constants import DATA_DIR, USER_IDS

def get_user_wpm(uid):
    df = pd.read_csv(DATA_DIR+'/user' + str(uid) + '/' + str(uid)  +'-tasks.csv', index_col='taskid', sep=';')
    
    def count_words(sen):
        l = sen.split(' ')
        while '' in l:
            l.remove('')
        return len(l)

    df['amount_words'] = df['result'].apply(count_words)

    df['wpm'] = (df['amount_words'] / (df['needed_time'] - df['time_generating'])) * 60

    return df.loc[:,['task', 'method', 'wpm']].set_index(['task', 'method'])


def get_avg_wpm():
    df = get_user_wpm(USER_IDS[0])
    for i in range(1, len(USER_IDS)):
        df += get_user_wpm(USER_IDS[0])
    df['wpm'] = df['wpm'] / len(USER_IDS)
    return df