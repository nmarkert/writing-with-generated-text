# Guide on generating:
# https://huggingface.co/blog/how-to-generate
import random
import time
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

mock_sentences = [
    'The quick brown fox jumps over the lazy dog.',
    'Today I will stay at home coding, because the weather is bad.',
    'I\'m hungry! Let\'s order some food. This new Italian is very good.',
    'Do you like to go to the soccer match with me today?'
]
def get_mock_sentence():
    return mock_sentences[random.randint(0, len(mock_sentences)-1)].split(' ')


class Generator:
    def __init__(self):
        self.index = 0
        self.sentence = []
        self.model_loaded = False
        self.model = None
        self.tokenizer = None
    

    def load_model(self):
        if self.model_loaded:
            return
        print('Started loading the model')
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        #add the EOS token as PAD token to avoid warnings
        self.model = GPT2LMHeadModel.from_pretrained("gpt2-medium", pad_token_id=self.tokenizer.eos_token_id)
        print('Finished loading')
        self.model_loaded = True
    

    def generate_sentence(self, keywords):
        self.load_model()
        print('Started generating a sentence')
        t1 = time.perf_counter()

        input_ids = self.tokenizer.encode(keywords, return_tensors='pt')
        t2 = time.perf_counter()
        #print('- ' + str(t2-t1) + ' seconds needed for Encoding')

        sample_output = self.model.generate(
            input_ids, 
            do_sample=True,
            min_length=40, 
            max_length=60,
            top_p=0.80, # sample only from 80% most likely words
            top_k=50, # in adition set top_k to 50
            num_return_sequences = 1,
        )
        t1 = time.perf_counter()
        print('- ' + str(t1-t2) + ' seconds needed for Generating')

        out = self.tokenizer.decode(sample_output[0], skip_special_tokens=True).split(' ')
        t2 = time.perf_counter()
        #print('- ' + str(t2-t1) + ' seconds needed for Decoding')

        return out
    

    def generate_multiple_options(self, pre, amount):
        self.load_model()
        pre_list = pre.split(' ')
        print('- Started generating a sentence')
        t1 = time.perf_counter()

        input_ids = self.tokenizer.encode(pre, return_tensors='pt')
        t2 = time.perf_counter()
        #print('- ' + str(t2-t1) + ' seconds needed for Encoding')

        sample_outputs = self.model.generate(
            input_ids, 
            do_sample=True,
            min_length=len(pre_list)+5, 
            max_length=len(pre_list)+10,
            top_p=0.80, # sample only from 80% most likely words
            top_k=50, # in adition set top_k to 50
            num_return_sequences = amount
        )
        t1 = time.perf_counter()
        print('- ' + str(t1-t2) + ' seconds needed for Generating')

        out=list()
        for sample_output in sample_outputs:
            sample = self.tokenizer.decode(sample_output, skip_special_tokens=True).split(' ')
            out.append(sample[len(pre_list):])
        t2 = time.perf_counter()
        #print('- ' + str(t2-t1) + ' seconds needed for Decoding')
        
        return out
        

    def create_sentence(self, keywords, mock_sentence=False):
        self.sentence = []
        if mock_sentence or keywords == '':
            self.sentence = get_mock_sentence()
        else:
            self.sentence = self.generate_sentence(keywords)
        return self.sentence
        
        
    def getAt(self, i):
        if i == -1:
            return ''
        if i >= len(self.sentence):
            return '\\eof'
        else:
            return self.sentence[i]



def test1():
    g = Generator()
    answer = 'y'
    while answer == 'y':
        g.create_sentence('I was playing with my dog, when')
        for i in range(-1, 10):
            print(g.getAt(i))
        
        answer = input('You want to try again? (y)(n) ')

def test2():
    g = Generator()
    g.load_model()
    answer = ''
    pre = 'I was playing with my dog'
    while not answer == 'exit':
        print(pre)
        sentences = g.generate_multiple_options(pre, 3)
        print('----- Choose:')
        for i, sen in enumerate(sentences):
            print('['+ str(i) + '] ', sen)
        index = int(input())
        for w in sentences[index]:
            pre += ' ' + w

if __name__ == "__main__":
    test2()