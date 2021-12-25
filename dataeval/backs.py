from constants import USER_IDS, task_file, log_file, boxplot_by_method, avg_by_method
from wpm import textlen_user
import numpy as np

def amount_backs_user_task(uid, tid):
    df = log_file(uid, tid)
    values = df['Action'].value_counts()
    if 'BACK' in values:
        return df['Action'].value_counts()['BACK']
    else:
        return 0

def amount_backs_user(uid):
    df = task_file(uid)

    def get_amount(row):
        return amount_backs_user_task(uid, row.name)
    df['amount_backs'] = df.apply(get_amount, axis=1)

    df = df.loc[:,['method', 'task', 'amount_backs']].set_index(['method', 'task'])
    df = df.sort_values(by=['method', 'task'], ascending=True)
    return df

def backs_textlen_ratio_user(uid):
    df = amount_backs_user(uid)
    df['text_len'] = textlen_user(uid)['text_len']
    df['ratio'] = df['amount_backs'] / df['text_len']
    return df

def backs_textlen_ratio_avg():
    df = backs_textlen_ratio_user(USER_IDS[0])
    for uid in USER_IDS[1:]:
        df += backs_textlen_ratio_user(uid)
    df['amount_backs'] = df['amount_backs'] / len(USER_IDS)
    df['text_len'] = df['text_len'] / len(USER_IDS)
    df['ratio'] = df['ratio'] / len(USER_IDS)
    return df


def backsequs_user_task(uid, tid):
    df = log_file(uid, tid)
    sequs = list()
    in_sequ = False
    c = 0
    for act in df['Action']:
        if in_sequ:
            if act == 'BACK':
                c += 1
            else:
                in_sequ = False
                sequs.append(c)
                c = 0
        else:  
            if act == 'BACK':
                in_sequ = True
                c = 1
            else:
                continue
    if in_sequ:
        sequs.append(c)
    return sequs

def backsequs_user(uid):
    df = task_file(uid)

    def get_amount(row):
        return len(backsequs_user_task(uid, row.name))
    def get_avg_len(row):
        sequs = backsequs_user_task(uid, row.name)
        if len(sequs) == 0:
            return 0
        else:
            return sum(sequs)/len(sequs)
    df['amount_backsequs'] = df.apply(get_amount, axis=1)
    df['avg_len_backsequs'] = df.apply(get_avg_len, axis=1)

    df = df.loc[:,['method', 'task', 'amount_backsequs', 'avg_len_backsequs']].set_index(['method', 'task'])
    df = df.sort_values(by=['method', 'task'], ascending=True)
    return df

def backsequs_textlen_ratio_user(uid):
    df = backsequs_user(uid)
    df['text_len'] = textlen_user(uid)['text_len']
    df['ratio'] = df['amount_backsequs'] / df['text_len']
    return df

def backsequs_avg(info=True):
    if info:
        print('### Average Length of Backsequenses and ratio of sequences per character ###')
    df = backsequs_textlen_ratio_user(USER_IDS[0])
    for uid in USER_IDS[1:]:
        df += backsequs_textlen_ratio_user(uid)
    df['ratio'] = df['ratio'] / len(USER_IDS)
    df['avg_len_backsequs'] = df['avg_len_backsequs'] / len(USER_IDS)
    return df.loc[:, ['avg_len_backsequs', 'ratio']]

def amount_backs_boxplot(save=False):
    boxplot_by_method(amount_backs_user, 'amount_backs', 
                        title='Amount of Backspace used', 
                        showfliers=False, 
                        save=save, 
                        filename='act_len_ratio')

def backs_textlen_ratio_boxplot(save=False):
    boxplot_by_method(backs_textlen_ratio_user, 'ratio', 
                        title='4)  Ratio Amount of Backspaces per character', 
                        showfliers=False, 
                        save=save, 
                        filename='backs_len_ratio')

def amount_backsequs_textlen_ratio_boxplot(save=False):
    boxplot_by_method(backsequs_textlen_ratio_user, 'ratio', 
                        title='5)  Ratio Amount of Backspace-Sequences per character', 
                        showfliers=False, 
                        save=save, 
                        filename='backseque_len_ratio')

def backsequs_len_boxplot(save=False):
    boxplot_by_method(backsequs_textlen_ratio_user, 'avg_len_backsequs', 
                        title='6)  Length of Backspace-Sequences (in characters)', 
                        showfliers=False, 
                        save=save, 
                        filename='backseques_length')

if __name__ == '__main__':
    #backs_textlen_ratio_boxplot(True)
    amount_backsequs_textlen_ratio_boxplot()
    #backsequs_len_boxplot(True)#
    #print(avg_by_method(backsequs_avg))
    #print(avg_by_method(backs_textlen_ratio_avg))