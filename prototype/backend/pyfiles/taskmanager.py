import time
from pyfiles.ratings import Ratings
from pyfiles.logger import InputLogger
from pyfiles.constants import METHODS, MIN_TEXT_LENGTH, TASKS

class Task:

    def __init__(self, id, desc, method):
        self.id = id
        self.desc = desc
        self.method = method
        self.result = str()
        self.ratings = Ratings(self.id)
        self.logger = InputLogger(self.id)
        self.last = False # Flag if the task is the last one
        self.t_start, self.t_end = None, None
        self.time_generating = 0

    def to_json(self):
        return {
            'desc': TASKS[self.desc],
            'method_name': METHODS[self.method],
            'method_id': self.method,
            'result': self.result,
            'last': self.last,
            'min_len': MIN_TEXT_LENGTH
        }
    
    def start_timer(self):
        if self.t_start == None:
            self.t_start = time.perf_counter()

    def end_timer(self):
        self.t_end = time.perf_counter()

    def add_generating_time(self, t):
        self.time_generating += t

    def needed_time(self):
        if self.t_start != None and self.t_end != None:
            return self.t_end - self.t_start
        else:
            return None

    def set_result(self, result):
        self.result = result
    
    def set_rating(self, quest, rating):
        self.ratings.set_rating(quest, rating)
    
    def log(self, sen):
        self.logger.log_sen(sen)

    def to_csv(self):
        return str(self.id) + ';' + str(self.desc) + ';' + str(self.method) + ';' + self.result.replace('\n','\\n').replace(';', ',') + ';' \
                + str(self.needed_time()) + ';' + str(self.time_generating)
    

tasks = list()

def fill_tasks(uid):
    order_tasks = [[0, 1], 
                   [1, 0]]
    order_methods = [[0, 1, 2],
                     [2, 0, 1],
                     [1, 2, 0]]

    tasks.clear()
    i = 0
    for task in order_tasks[uid%2]:
        for method in order_methods[uid%3]:
            tasks.append(
                Task(str(uid)+str(i), task, method)
            )
            i += 1
    tasks[-1].last = True


def add_task(desc, method):
    tasks.append(
        Task(len(tasks), desc, method)
    )


class Current:
    def __init__(self):
        self.id = 0
        self.active = False
    
    def set_curr(self, curr):
        self.id = curr
        self.active = True
    
    def not_active(self):
        self.active = False

    def get_curr(self):
        if self.active:
            return self.id
        else:
            return None