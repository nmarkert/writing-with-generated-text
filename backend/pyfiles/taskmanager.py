import time
from ratings import Ratings

class Task:

    def __init__(self, id, desc, method):
        self.id = id
        self.desc = desc
        self.method = method
        self.result = str()
        self.ratings = Ratings(self.id)
        self.last = False # Flag if the task is the last one
        self.t_start, self.t_end = None, None

    def to_json(self):
        return {
            'desc': self.desc,
            'method': self.method,
            'result': self.result,
            'last': self.last
        }
    
    def start_timer(self):
        self.t_start = time.perf_counter()

    def end_timer(self):
        self.t_end = time.perf_counter()

    def needed_time(self):
        if self.t_start != None and self.t_end != None:
            return self.t_end - self.t_start
        else:
            return None

    def set_result(self, result):
        self.result = result
    
    def set_rating(self, quest, rating):
        self.ratings.set_rating(quest, rating)

    def to_csv(self):
        return str(self.id) + ';' + self.desc + ';' + str(self.method) + ';' + self.result.replace('\n','\\n').replace(';', ',') + ';' + str(self.needed_time())
    

# Concrete Task
T1 = 'Write an email ....' 

# Open Task
T2 = 'Write a blog post ....'

tasks = list()

def fill_tasks(uid):
    order_tasks = [[T1, T2], 
                   [T2, T1]]
    order_methods = [[0, 1, 2],
                     [2, 0, 1],
                     [1, 2, 0]]

    tasks.clear()
    i = 0
    for task in order_tasks[uid%2]:
        for method in order_methods[uid%3]:
            tasks.append(
                Task(int(str(uid)+str(i)), task, method)
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
    
    def set_curr(self, curr):
        self.id = curr
    
    def get_curr(self):
        return self.id