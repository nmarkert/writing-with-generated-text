from flask import Flask, Response, request, json
import generator
#import redis

app = Flask(__name__)
#cache = redis.Redis(host='redis', port=6379)

g = generator.Generator()

@app.route('/api', methods=['POST'])
def request_next():
    request_data = json.loads(request.data)
    i = request_data['id']
    return {'word': g.getAt(i)}


@app.route('/generate', methods=['POST'])
def generate_sentene():
    request_data = json.loads(request.data)
    keyword = request_data['content']
    print(keyword)
    return {'ready': g.create_sentence(keyword)}


@app.route('/generate_new', methods=['POST'])
def generate_new_sentene():
    request_data = json.loads(request.data)
    sentence = request_data['content']
    print(sentence)
    index = len(sentence.split(' '))
    return {'ready': g.create_sentence(sentence),
            'index': index}

app.run(debug=False)