import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from constants import USER_IDS, task_file, QUESTIONS, diverging_bar


def question_user(qid, uid):
    df = task_file(uid)

    ques = 'question' + str(qid)

    df = df.loc[:,['task', 'method', ques]].set_index(['method', 'task'])
    df = df.sort_values(by=['method', 'task'], ascending=True)

    return df


def transform(df):
    answers = ['no_answ','str_disagree', 'disagree', 'neither', 'agree', 'str_agree']
    df[answers] = 0

    def vectorize_answer(row):
        answ = answers[row[0]]
        row[answ] += 1

    df.apply(vectorize_answer, axis=1)
    df = df.drop(df.columns[0], axis=1)

    return df


def question_answers(qid, info=True):
    if info:
        print('###', QUESTIONS[qid], '###')
    df = transform(question_user(qid, USER_IDS[0]))
    for uid in USER_IDS[1:]:
        df +=  transform(question_user(qid, uid))

    return df


def question_hist_by_method(qid):
    df = question_answers(qid, False)
    labels = df.columns
    #labels = ['No Answer', 'Strongly Disagree', 'Disagree', 'Neither', 'Agree', 'Strongly Agree']

    x = np.arange(len(labels))  # the label locations
    width = 0.35/2  # the width of the bars
    
    f = [-1, 0, 1]
    methods = ['Version0', 'Version1', 'Version2']
    max_amount = 0

    fig, ax = plt.subplots()
    for m in range(3):
        y = np.zeros(len(labels))
        for t in range(2):
            y += df.loc[(m, t)]
        max_amount = max(int(max(y)), max_amount)
        ax.bar(x+f[m]*width, y, width, label=methods[m])

    ax.set_title('Answers by Method')
    ax.set_yticks(range(max_amount+1))
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    fig.tight_layout()
    plt.show()


def question_diverging_bar(qid, save=False):
    df = question_answers(qid, False)
    df = df.drop('no_answ', axis=1)

    idxs = list()
    for i in range(3):
        for j in range(2):
            idxs.append("Version " + str(i) + " - Task " + str(j))
    
    names = ['Strongly disagree', 'Disagree',
            'Neither agree nor disagree',
            'Agree', 'Strongly agree']
    
    if save:
        diverging_bar(df, idxs, names, True, 'question' + str(qid))
    else:
        diverging_bar(df, idxs, names, False)


def question_diverging_bar_by_method(qid, save=False):
    df = question_answers(qid, False)
    df = df.drop('no_answ', axis=1)

    df = df.groupby('method').sum()
    
    idxs = list()
    for i in range(3):
        idxs.append('Version ' + str(i))

    names = ['Strongly disagree', 'Disagree',
            'Neither agree nor disagree',
            'Agree', 'Strongly agree']
    
    if save:
        diverging_bar(df, idxs, names, True, 'question' + str(qid) + '_by_method')
    else:
        diverging_bar(df, idxs, names, False)



if __name__ == '__main__':    
    question_diverging_bar_by_method(0, True)
    #for i in range(6):
    #    print(question_answers(i))
