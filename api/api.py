from flask import Flask, Response, request, json
import generator

app = Flask(__name__)

g = generator.Generator()

@app.route('/api', methods=['POST'])
def request_next():
    request_data = json.loads(request.data)
    i = request_data['id']
    return {'word': g.getAt(i)}
