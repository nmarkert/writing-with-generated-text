import pandas as pd

DATA_DIR = 'D:/Daten (D)/Uni/6. Semester/BA-Arbeit/data'

def get_words_per_minute(uid):
    df = pd.read_csv(DATA_DIR+'/' + str(uid) +'-tasks.csv', index_col='taskid', sep=';')
    
    def count_words(sen):
        l = sen.split(' ')
        while '' in l:
            l.remove('')
        return len(l)

    df['amount_words'] = df['result'].apply(count_words)

    df['wpm'] = (df['amount_words'] / df['needed_time']) * 60

    return df.loc[:,['description', 'method', 'wpm']]


print(get_words_per_minute(0))