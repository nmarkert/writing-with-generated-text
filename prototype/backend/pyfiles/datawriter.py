import os, os.path
from pyfiles.constants import DATA_DIR, TASK_FILE_HEADER

class DataWriter:

    def __init__(self):
        self.DATA_DIR = DATA_DIR

    def create_data_dir(self):
        if not os.path.isdir(self.DATA_DIR):
            os.mkdir(self.DATA_DIR)
    
    def create_user_dir(self):
        self.create_data_dir()
        if not os.path.isdir(self.USER_DIR):
            os.mkdir(self.USER_DIR)


    def set_user_id(self, uid):
        self.set_user_dir(uid)
        self.set_tasks_filename(uid)
        self.set_ratings_filename(uid)
        self.set_log_dir(uid)
    
    def set_user_dir(self, uid):
        self.USER_DIR = self.DATA_DIR + '/user' + str(uid)
    

    # Everything for the tasks file ----------------------
    def set_tasks_filename(self, uid):
        self.TASKS_FILENAME = self.USER_DIR + '/' + str(uid) + '-tasks.csv'

    def write_tasks_fileheader(self):
        self.create_user_dir()
        if os.path.isfile(self.TASKS_FILENAME):
            return
        with open(self.TASKS_FILENAME, 'w') as f:
            f.write(TASK_FILE_HEADER)
        
    def store_task(self, task):
        self.write_tasks_fileheader()
        with open(self.TASKS_FILENAME, 'a') as f:
            f.write(task.to_csv() + ';' + task.ratings.to_csv() + '\n')
            print('Stored task to:', self.TASKS_FILENAME)
    

    # Everything for the log files ----------------------
    def set_log_dir(self, uid):
        self.LOG_DIR = self.USER_DIR + '/' + str(uid) + '-logs'
    
    def create_log_dir(self):
        if not os.path.isdir(self.LOG_DIR):
            os.mkdir(self.LOG_DIR)
    
    def write_log(self, tid, log):
        self.create_log_dir()
        path = self.LOG_DIR + '/task' + str(tid) + '.csv'
        log.to_csv(path, index=False, header=True, sep=';')
