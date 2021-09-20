import pandas as pd
from constants import DATA_DIR, USER_IDS


def question_user(qid, uid):
    user_dir = DATA_DIR + '/user' + str(uid) + '/' + str(uid)
    df = pd.read_csv(user_dir + '-tasks.csv', index_col='taskid', sep=';')

    ques = 'question' + str(qid)

    return df.loc[:,['task', 'method', ques]].set_index(['task', 'method'])


def transform(df):
    answers = ['no_answ','str_disagree', 'disagree', 'neither', 'agree', 'str_agree']
    for a in answers:
        df[a] = 0
    
    def vectorize_answer(row):
        answ = answers[row[0]]
        row[answ] += 1

    df.apply(vectorize_answer, axis=1)
    df = df.drop(df.columns[0], axis=1)

    return df


def question_answers(qid):
    df = transform(question_user(qid, USER_IDS[0]))
    for uid in USER_IDS[1:]:
        df +=  transform(question_user(qid, uid))

    return df


print(question_user(0, 98))
print(question_user(0, 99))

d = question_answers(0)
print(d)
