from flask import Flask, Response, request, json
import generator

app = Flask(__name__)

g = generator.Generator()

@app.route('/api/get_next', methods=['POST'])
def request_next():
    request_data = json.loads(request.data)
    i = request_data['id']
    return {'word': g.getAt(i)}


@app.route('/api/generate', methods=['POST'])
def generate_sentene():
    request_data = json.loads(request.data)
    keyword = request_data['content']
    print(keyword)
    return {'ready': g.create_sentence(keyword)}


@app.route('/api/generate_new', methods=['POST'])
def generate_new_sentene():
    request_data = json.loads(request.data)
    sentence = request_data['content']
    print(sentence)
    index = len(sentence.split(' '))
    return {'ready': g.create_sentence(sentence),
            'index': index}
