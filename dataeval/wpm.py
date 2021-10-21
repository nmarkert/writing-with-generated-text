from constants import USER_IDS, task_file


def textlen_user(uid, include_times=False):
    df = task_file(uid)
    def count_words(sen):
        l = sen.split(' ')
        while '' in l:
            l.remove('')
        return len(l)

    df['text_len'] = df['result'].apply(count_words)

    cols = ['task', 'method', 'text_len']
    if include_times:
        cols.extend(['needed_time', 'time_generating'])

    df = df.loc[:,cols].set_index(['method', 'task'])
    df = df.sort_values(by=['method', 'task'], ascending=True)

    return df


def textlen_avg(info=True):
    if info:
        print('### Average text length (in words) ###')
    df = textlen_user(USER_IDS[0])
    for uid in USER_IDS[1:]:
        df += textlen_user(uid)
    df['text_len'] = df['text_len'] / len(USER_IDS)
    return df


def wpm_user(uid):
    df = textlen_user(uid, True)

    df['wpm'] = (df['text_len'] / (df['needed_time'] - df['time_generating'])) * 60

    return df.loc[:, ['wpm']]


def wpm_avg():
    print('### Average Words per minute ###')
    df = wpm_user(USER_IDS[0])
    for uid in USER_IDS[1:]:
        df += wpm_user(uid)
    df['wpm'] = df['wpm'] / len(USER_IDS)
    return df


if __name__ == '__main__':  
    print(wpm_avg())
    print(textlen_avg())