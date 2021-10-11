import os
import pandas as pd

# All ids of users for which data is stored
# Maybe store a text file in data with all the ids
USER_IDS = [12, 13, 14, 15, 17]
#USER_IDS = [13, 14]

# Directory for the data to evaluate
DATA_DIR = os.getcwd() + '/../prototype/backend/real_data' # Data dir for real values

# Gets the task file based on the userId
def task_file(uid):
    return pd.read_csv(DATA_DIR +'/user' + str(uid) + '/' + str(uid)  +'-tasks.csv', index_col='taskid', sep=';')

# Gets the log file based on the userId and the taskId
def log_file(uid, tid):
    if tid < 6:
        tid = uid*10 + tid
    return pd.read_csv(DATA_DIR +'/user' + str(uid) + '/' + str(uid)  + '-logs/task' + str(tid) + '.csv', sep=';')