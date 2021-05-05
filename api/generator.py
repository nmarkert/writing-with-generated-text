import random
mock_sentences = [
    'The quick brown fox jumps over the lazy dog.',
    'Today I will stay at home coding, because the weather is bad.',
    'I\'m hungry! Let\'s order some food. This new Italian is very good.',
    'Do you like to go to the soccer match with me today?'
]

class Generator:
    def __init__(self):
        self.index = 0
        self.sentence = []
    
    def create_sentence(self):
        self.sentence = mock_sentences[random.randint(0, len(mock_sentences)-1)].split(' ')
        
    def getNext(self, i):
        print(i)
        if i == -1:
            self.create_sentence()
            self.index = 0
            return ''
        if self.index >= len(self.sentence):
            return ''
        else:
            self.index += 1
            return self.sentence[self.index-1]
        
    def getAt(self, i):
        if i == -1:
            self.create_sentence()
            return ''
        if i >= len(self.sentence):
            return ''
        else:
            return self.sentence[i]


if __name__ == "__main__":
    g = Generator()
    for i in range(-1, 5):
        print(g.getNext(i))