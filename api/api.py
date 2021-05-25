from flask import Flask, Response, request, json
import generator

app = Flask(__name__)

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