import os
from numpy.core.numeric import outer
import pandas as pd
import plotly.graph_objects as go

# All ids of users for which data is stored
# Maybe store a text file in data with all the ids
USER_IDS = list(range(12, 33))
USER_IDS.remove(29)

# Directory for the data to evaluate
DATA_DIR = os.getcwd() + '/../prototype/backend/real_data' # Data dir for real values

# Directory for the output
OUTPUT_DIR = os.getcwd() + '/plots'

# Gets the task file based on the userId
def task_file(uid):
    return pd.read_csv(DATA_DIR +'/user' + str(uid) + '/' + str(uid)  +'-tasks.csv', index_col='taskid', sep=';')

# Gets the log file based on the userId and the taskId
def log_file(uid, tid):
    if tid < 6:
        tid = uid*10 + tid
    return pd.read_csv(DATA_DIR +'/user' + str(uid) + '/' + str(uid)  + '-logs/task' + str(tid) + '.csv', sep=';')


# The questions after each task
QUESTIONS = [
    'I am satisfied with the text.',
    'It was easy for me to write the text.',
    'I feel like I am the author of the text.',
    'The interaction method was suitable for this task.',
    'The interaction method helped me writing the text.',
    'The interaction method influenced the wording of the text.'
]

def diverging_bar(df, idxs, names, save=False, filename='', format='png'):
    diverging = go.Figure()

    n1 = -1*df.iloc[:, 2] / 2
    n2 = n1 - df.iloc[:, 1]
    n3 = n2 - df.iloc[:, 0]
    p1 = -1* n1
    p2 = p1 + df.iloc[:, 3]

    positions = [n3, n2, n1, p1, p2]

    colors = ['firebrick','lightcoral','darkgrey','cornflowerblue', 'darkblue']

    for i, col in enumerate(df.columns):
        diverging.add_trace(go.Bar( x=df[col],
                                    y=idxs,
                                    base=positions[i],
                                    orientation='h',
                                    name=names[i],
                                    marker={'color': colors[i]} ))
    
    # Specifying the layout of the plot
    diverging.update_layout(barmode='relative',
                        height=400,
                        width=700,
                        yaxis_autorange='reversed',
                        bargap=0.5,
                        legend_orientation='v',
                        legend_x=1, legend_y=0)
    
    if save:
        if not os.path.exists(OUTPUT_DIR):
            os.mkdir(OUTPUT_DIR)
        diverging.write_image(OUTPUT_DIR + '/' + filename + '.' + format)
    else:
        diverging.show()
