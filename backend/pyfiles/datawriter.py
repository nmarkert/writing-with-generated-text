import os, os.path
import time
from ratings import questions
PATH = os.getcwd()


class DataWriter:

    def __init__(self):
        self.DATA_DIR = PATH + '/data'

    def create_data_dir(self):
        if not os.path.isdir(self.DATA_DIR):
            os.mkdir(self.DATA_DIR)

    def set_filenames(self, uid):
        self.set_tasks_filename(uid)
        self.set_ratings_filename(uid)
    

    # Everything for the tasks file ----------------------
    def set_tasks_filename(self, uid):
        self.TASKS_FILENAME = self.DATA_DIR + '/' + str(uid) + '-tasks.csv'
        self.write_tasks_fileheader()

    def write_tasks_fileheader(self):
        if os.path.isfile(self.TASKS_FILENAME):
            return
        header = 'time;taskid;description;method;result;needed_time\n'
        with open(self.TASKS_FILENAME, 'w') as f:
            f.write(header)
        
    def store_task(self, task):
        with open(self.TASKS_FILENAME, 'a') as f:
            f.write(time.ctime() + ';' + task.to_csv() + '\n')
    

    # Everything for the ratings file ----------------------
    def set_ratings_filename(self, uid):
        self.RATINGS_FILENAME = self.DATA_DIR + '/' + str(uid) + '-ratings.csv'
        self.write_ratings_fileheader()

    def write_ratings_fileheader(self):
        if os.path.isfile(self.RATINGS_FILENAME):
            return
        header = 'taskid;'
        for i in range(len(questions)):
            header += 'question' + str(i) + ';'
        header = header[:-1] + '\n'
        with open(self.RATINGS_FILENAME, 'w') as f:
            f.write(header)
        
    def store_ratings(self, ratings):
        with open(self.RATINGS_FILENAME, 'a') as f:
            f.write(ratings.to_csv() + '\n')
