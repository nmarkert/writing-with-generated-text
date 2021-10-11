from constants import USER_IDS, task_file, log_file


def amount_actions_user_task(uid, tid, method=-1, amount_new_opts=-1):
    df = log_file(uid, tid)
    df = df.dropna(axis=0)

    if method == -1:
        method = task_file(uid).loc[tid, 'method']

    if method == 0 or method == 1:
        return len(df)

    elif method == 2:
        if amount_new_opts == -1:
            amount_new_opts = task_file(uid).loc[tid, 'amount_new_opts']
        return len(df) + amount_new_opts

    else:
        return None


def amount_actions_user(uid):
    df = task_file(uid)

    def get_amount(row):
        return amount_actions_user_task(uid, row.name, row['method'], row['amount_new_opts'])
    
    df['amount_actions'] = df.apply(get_amount, axis=1)
    
    df = df.loc[:,['method', 'task', 'amount_actions']].set_index(['method', 'task'])
    df = df.sort_values(by=['method', 'task'], ascending=True)

    return df


def amount_actions_avg():
    print('### Average Actions performed ###')
    df = amount_actions_user(USER_IDS[0])
    for uid in USER_IDS[1:]:
        df += amount_actions_user(uid)
    df['amount_actions'] = df['amount_actions'] / len(USER_IDS)
    return df


print(amount_actions_avg())