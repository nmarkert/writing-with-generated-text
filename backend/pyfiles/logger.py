import time
import pandas as pd

class InputLogger:
    def __init__(self, tid):
        self.tid = tid
        self.log = pd.DataFrame(columns=['Time', 'Perf_Time', 'Action'])
        self.curr_sen = ''
    
    #TODO maybe better calculate what was typed
    def get_action(self, old_sen, new_sen):
        if len(new_sen) > len(old_sen):
            return new_sen[len(old_sen):]
        elif len(new_sen) < len(old_sen):
            return 'BACK'
        else:
            return ''

    def log_sen(self, sen):
        t = time.localtime()
        ts = str(t.tm_hour) + ':' + str(t.tm_min) + ':' + str(t.tm_sec)
        perft = time.perf_counter()
        act = self.get_action(self.curr_sen, sen)
        if act == ' ':
            act = 'SPACE'
        self.curr_sen = sen
        self.log.loc[len(self.log)] = [ts, perft, act]

    def get_log(self):
        return self.log