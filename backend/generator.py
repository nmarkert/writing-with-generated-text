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
        print('Start loading')
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        #add the EOS token as PAD token to avoid warnings
        self.model = GPT2LMHeadModel.from_pretrained("gpt2-medium", pad_token_id=self.tokenizer.eos_token_id)
        print('Finished loading')
        self.model_loaded = True
    

    def generate_sentence(self, keywords):
        if not self.model_loaded:
            self.load_model()
        print('Started generating a sentence')
        start_time = time.perf_counter()

        input_ids = self.tokenizer.encode(keywords, return_tensors='pt')

        sample_output = self.model.generate(
            input_ids, 
            do_sample=True,
            min_length=40, 
            max_length=60,
            top_p=0.80, # sample only from 80% most likely words
            top_k=50, # in adition set top_k to 50
        )

        end_time = time.perf_counter()
        print('Finished generation. Needed Time: '+ str(end_time-start_time) + ' seconds')
        return self.tokenizer.decode(sample_output[0], skip_special_tokens=True)
    

    def create_sentence(self, keywords, mock_sentence=False):
        self.sentence = []
        if mock_sentence or keywords == '':
            self.sentence = get_mock_sentence()
        else:
            self.sentence = self.generate_sentence(keywords).replace('\n', ' ').split(' ')
        print(self.sentence)
        return self.sentence
        
    def getNext(self, i):
        if i == -1:
            self.index = 0
            return ''
        if self.index >= len(self.sentence):
            return ''
        else:
            self.index += 1
            return self.sentence[self.index-1]
        
    def getAt(self, i):
        if i == -1:
            return ''
        if i >= len(self.sentence):
            return '\\eof'
        else:
            return self.sentence[i]

    def sentence_is_generated(self):
        return len(self.sentence) > 0


if __name__ == "__main__":
    g = Generator()
    answer = 'y'
    while answer == 'y':
        g.create_sentence('I was playing with my dog, when')
        for i in range(-1, 10):
            print(g.getAt(i))
        
        answer = input('You want to try again? (y)(n) ')