# Guide:
# https://huggingface.co/blog/how-to-generate

import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# add the EOS token as PAD token to avoid warnings
model = TFGPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)


# encode context the generation is conditioned on
input_ids = tokenizer.encode('I enjoy walking with my cute dog', return_tensors='tf')


def greedySearch():
    # generate text until the output length (which includes the context length) reaches 50  
    greedy_output = model.generate(input_ids, max_length=50)

    print(tokenizer.decode(greedy_output[0], skip_special_tokens=True))


def beamSearch():
    # activate beam search and early_stopping
    beam_output = model.generate(
        input_ids, 
        max_length=50, 
        num_beams=5, 
        no_repeat_ngram_size=2, # set no_repeat_ngram_size to 2
        early_stopping=True
    )

    print(tokenizer.decode(beam_output[0], skip_special_tokens=True))


def sample():
    # set seed to reproduce results. Feel free to change the seed though to get different results
    tf.random.set_seed(0)

    # activate sampling and deactivate top_k by setting top_k sampling to 0
    sample_output = model.generate(
        input_ids, 
        do_sample=True, 
        max_length=50, 
        top_k=0,
        temperature=0.7 # use temperature to decrease the sensitivity to low probability candidates
                        # when setting temperature to 0, it is the same as greedy
    )

    print(tokenizer.decode(sample_output[0], skip_special_tokens=True))


def topKSample():
    tf.random.set_seed(0)

    # set top_k to 50
    sample_output = model.generate(
        input_ids, 
        do_sample=True, 
        max_length=50, 
        top_k=50
    )

    print(tokenizer.decode(sample_output[0], skip_special_tokens=True))


def topPSample():
    tf.random.set_seed(0)

    # sample only from 92% most likely words
    sample_outputs = model.generate(
        input_ids, 
        do_sample=True, 
        max_length=50,
        top_p=0.92, # 0 < top_p < 1 
        top_k=50, # in adition set top_k to 50
        num_return_sequences=3 # generate more than one option
    )

    for i, sample_output in enumerate(sample_outputs):
        print("{}: {}".format(i, tokenizer.decode(sample_output, skip_special_tokens=True)))



print("Output:\n" + 100 * '-')
topPSample()