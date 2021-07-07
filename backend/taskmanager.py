import time

class Task:

    def __init__(self, id, desc, method):
        self.id = id
        self.desc = desc
        self.method = method
        self.result = ''
        self.rating = 0

    def to_json(self):
        return {
            'desc': self.desc,
            'method': self.method,
            'result': self.result
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
    
    def set_rating(self, rating):
        self.rating = rating



tasks = list()

def add_task(desc, method):
    tasks.append(
        Task(len(tasks), desc, method)
    )

add_task('Write a Email to a friend.', 0)
#add_task('Write a Email to your boss.', 0)

add_task('Write a Email to a friend.', 1)
#add_task('Write a Email to your boss.', 1)

add_task('Write a Email to a friend.', 2)
#add_task('Write a Email to your boss.', 2)

class Current:
    def __init__(self):
        self.id = 0
    
    def set_curr(self, curr):
        self.id = curr
    
    def get_curr(self):
        return self.id