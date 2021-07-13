questions = [
    'I am satisfied with my result.',
    'It was easy for me to write the text.'
]

class Ratings:
    def __init__(self, tid):
        self.tid = tid
        self.ratings = [0 for i in range(len(questions))]
    
    def set_rating(self, quest, rating):
        self.ratings[quest] = rating

    def to_csv(self):
        s = str(self.tid) + ';'
        for rating in self.ratings:
            s += str(rating) + ';'
        return s[:-1]