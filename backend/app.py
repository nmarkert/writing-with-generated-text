from random import random
from flask import Flask, Response, request, json
import generator

app = Flask(__name__)

g = generator.Generator()


@app.route('/api/generate', methods=['POST'])
def generate_sentence():
    request_data = json.loads(request.data)
    sentence = request_data['content']
    print(sentence)
    if sentence == '':
        index = 0
        mock = True
    else:
        index = len(sentence.split(' '))
        mock = False
    return {'sentence': g.create_sentence(sentence, mock),
            'index': index}


g.load_model()
print('Everything is ready')
app.run(debug=False)
