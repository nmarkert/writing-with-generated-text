from constants import USER_IDS, task_file


def generations_user(uid):
    df = task_file(uid)

    df = df.loc[:, ['task', 'method', 'amount_generations']].set_index(['method', 'task'])
    df = df.drop(index = (0,0))
    df = df.drop(index = (0,1))
    df = df.sort_values(by=['method', 'task'], ascending=True)

    return df


def generations_avg():
    df = generations_user(USER_IDS[0])
    for uid in USER_IDS[1:]:
        df += generations_user(uid)
    df['amount_generations'] = df['amount_generations'] / len(USER_IDS)

    return df



def new_options_user(uid):
    df = task_file(uid)
    
    df = df.loc[:, ['task', 'method', 'amount_new_opts']].set_index(['method', 'task'])
    for t in range(2):
        for m in range(2):
            df.drop(index=(m, t), inplace=True)
    df = df.sort_values(by=['method', 'task'], ascending=True)

    return df


def new_options_avg():
    df = new_options_user(USER_IDS[0])
    for uid in USER_IDS[1:]:
        df += new_options_user(uid)
    df['amount_new_opts'] = df['amount_new_opts'] / len(USER_IDS)

    return df


if __name__ == '__main__':      
    print(new_options_avg())