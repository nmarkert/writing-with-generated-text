from os import sep
import pandas as pd
from constants import DATA_DIR, USER_IDS

def question_user(qid, uid):
    user_dir = DATA_DIR + '/user' + str(uid) + '/' + str(uid)
    df = pd.read_csv(user_dir + '-tasks.csv', index_col='taskid', sep=';')
    #df_quest = pd.read_csv(user_dir + '-ratings.csv', index_col='taskid', sep=';')
    #df = df_task.append(df_quest)
    #df = pd.DataFrame([df_task, df_quest])
    
    return df.loc[:,['task', 'method', 'question0', 'question1']].set_index(['task', 'method'])


print(question_user(0, 22))