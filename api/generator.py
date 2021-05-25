import random
import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

mock_sentences = [
    'The quick brown fox jumps over the lazy dog.',
    'Today I will stay at home coding, because the weather is bad.',
    'I\'m hungry! Let\'s order some food. This new Italian is very good.',
    'Do you like to go to the soccer match with me today?'
]
def get_mock_sentence():
    return mock_sentences[random.randint(0, len(mock_sentences)-1)].split(' ')


tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# add the EOS token as PAD token to avoid warnings
model = TFGPT2LMHeadModel.from_pretrained("gpt2-medium", pad_token_id=tokenizer.eos_token_id)

def generate_sentence(keywords):
    input_ids = tokenizer.encode(keywords, return_tensors='tf')

    tf.random.set_seed(random.random())
    sample_output = model.generate(
        input_ids, 
        do_sample=True,
        min_length=20, 
        max_length=40,
        top_p=0.80, # sample only from 80% most likely words
        top_k=50, # in adition set top_k to 50
    )

    return tokenizer.decode(sample_output[0], skip_special_tokens=True)


class Generator:
    def __init__(self):
        self.index = 0
        self.sentence = []
    
    def create_sentence(self, keywords):
        self.sentence = []
        self.sentence = generate_sentence(keywords).replace('\n', ' ').split(' ')
        print(self.sentence)
        return True
        
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
    g.create_sentence('I was playing with my dog, when')
    for i in range(-1, 20):
        print(g.getAt(i))