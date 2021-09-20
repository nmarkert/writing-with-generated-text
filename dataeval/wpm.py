import pandas as pd
from constants import DATA_DIR, USER_IDS

def wpm_user(uid):
    df = pd.read_csv(DATA_DIR +'/user' + str(uid) + '/' + str(uid)  +'-tasks.csv', index_col='taskid', sep=';')
    
    def count_words(sen):
        l = sen.split(' ')
        while '' in l:
            l.remove('')
        return len(l)

    df['amount_words'] = df['result'].apply(count_words)

    df['wpm'] = (df['amount_words'] / (df['needed_time'] - df['time_generating'])) * 60

    return df.loc[:,['task', 'method', 'wpm']].set_index(['task', 'method'])


def wpm_avg():
    df = wpm_user(USER_IDS[0])
    for uid in USER_IDS[1:]:
        df += wpm_user(uid)
    df['wpm'] = df['wpm'] / len(USER_IDS)
    return df

print(wpm_avg())