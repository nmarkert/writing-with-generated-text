import os
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# All ids of users for which data is stored
# Maybe store a text file in data with all the ids
USER_IDS = list(range(12, 33))
USER_IDS.remove(29)

LOGEVAL = True
if (LOGEVAL):
    # Remove when evaluating Log-Data
    USER_IDS.remove(13) # Problems on V2
    USER_IDS.remove(30) # Done on Laptop

# Directory for the data to evaluate
DATA_DIR = os.getcwd() + '/../prototype/backend/real_data' # Data dir for real values

# Directory for the output
OUTPUT_DIR = os.getcwd() + '/plots'

# Directory for the input
INPUT_DIR = os.getcwd() + '/tables'

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

def avg_by_method(func):
    df = func()
    df = df.groupby(level='method').sum()
    df = df/2
    return df

def diverging_bar(df, idxs, names, title='', save=False, filename='', format='svg'):
    diverging = go.Figure()

    
    n1 = -1*df.iloc[:, 2] / 2
    n2 = n1 - df.iloc[:, 1]
    n3 = n2 - df.iloc[:, 0]
    p1 = -1* n1
    p2 = p1 + df.iloc[:, 3]

    b1 = -20
    x1 = 20+n3
    b2 = p2 + df.iloc[:, 4]
    x2 = 20-b2

    positions = [n3, n2, n1, p1, p2]

    colors = ['firebrick','lightcoral','darkgrey','cornflowerblue', 'darkblue']

    diverging.add_trace(go.Bar( x=x1,
                                    y=idxs,
                                    base=b1,
                                    orientation='h',
                                    marker={'color': 'rgba(0,0,0,0)',
                                    'line':{'width':0}},
                                    showlegend=False ))

    for i, col in enumerate(df.columns):
        diverging.add_trace(go.Bar( x=df[col],
                                    y=idxs,
                                    base=positions[i],
                                    orientation='h',
                                    name=names[i],
                                    marker={'color': colors[i]} ))

    diverging.add_trace(go.Bar( x=x2,
                                y=idxs,
                                base=b2,
                                orientation='h',
                                marker={'color': 'rgba(0,0,0,0)',
                                'line':{'width':0}},
                                showlegend=False ))
    
    # Specifying the layout of the plot
    diverging.update_layout(barmode='relative',
                        height=400,
                        width=700,
                        yaxis_autorange='reversed',
                        bargap=0.5,
                        legend_orientation='v',
                        legend_x=1.1, legend_y=0,
                        title=title,
                        plot_bgcolor ='white',
                        xaxis=dict(
                            tickmode = 'array',
                            tickvals = [-20, -15, -10, -5, 0, 5, 10, 15, 20],
                            ticktext = [20, 15, 10, 5, 0, 5, 10, 15, 20])
                        )
    diverging.update_xaxes(gridcolor='lightgrey', gridwidth=1, zerolinewidth=2, zerolinecolor='black', showline=True, mirror=True, linecolor='black')
    diverging.update_yaxes(showline=True, mirror=True, linecolor='black')

    if save:
        out = OUTPUT_DIR + '/' + format
        if not os.path.exists(out):
            os.mkdir(out)
        diverging.write_image(out + '/' + filename + '.' + format)
    else:
        diverging.show()


def boxplot_by_method(func, col_name, title='', showfliers=False,  save=False, filename='', format='png'):
    df = pd.DataFrame(columns=['V0', 'V1', 'V2'])

    for uid in USER_IDS:
        tmp = func(uid)
        for t in range(2):
            v = {'V0':0, 'V1':0, 'V2':0}
            for m in range(3):
                k = 'V' + str(m)
                v[k] = tmp.loc[(m, t), col_name]
            df = df.append(v, ignore_index=True)

    fig, ax = plt.subplots()
    bp = ax.boxplot(df, 
                    patch_artist=True,  # fill with color
                    labels=['Std. Input', 'Con. gen. Text', 'Writ. with Sugg.'],  # will be used to label x-ticks
                    showfliers=showfliers) # maybe set to false??

    colors = ['pink', 'lightblue', 'lightgreen']

    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)  

    for patch in bp['medians']:
        patch.set_linewidth(1.3) 

    ax.set_title(title)

    if save:
        out = OUTPUT_DIR + '/logging'
        if not os.path.exists(out):
            os.mkdir(out)
        plt.savefig(out + '/' + filename + '.' + format)
    else:
        plt.show()