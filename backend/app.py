import re
from flask import Flask, request, json
from pyfiles.generator import Generator
from pyfiles.taskmanager import tasks, fill_tasks, Current, SURVEY_LINK
from pyfiles.datawriter import DataWriter
from pyfiles.ratings import questions

app = Flask(__name__)

d = DataWriter()
g = Generator()
c = Current()


@app.route('/api/generate', methods=['POST'])
def generate_sentence():
    request_data = json.loads(request.data)
    sentence = request_data['content']

    index = len(sentence.split(' '))
    sen, t = g.generate_sentence(sentence)
    tasks[c.get_curr()].add_generating_time(t)

    return {'sentence': sen,
            'index': index}


@app.route('/api/generate_options', methods=['POST'])
def generate_options():
    request_data = json.loads(request.data)
    pre = request_data['pre_sentence']
    amount = 3
    sen, t = g.generate_multiple_options(pre, amount)
    tasks[c.get_curr()].add_generating_time(t)
    return {'sentences': sen}


@app.route('/api/user/<int:uid>') 
def set_user_id(uid):
    fill_tasks(uid)
    d.set_filenames(uid)
    return '', 204


@app.route('/api/questions')
def get_questions():
    return {'questions': questions}


@app.route('/api/task/<int:id>') 
def get_task(id):
    c.set_curr(id)
    return tasks[id].to_json()


@app.route('/api/task/<int:id>/start_timer') 
def start_timer(id):
    tasks[id].start_timer()
    return '', 204


@app.route('/api/task/<int:id>/end_timer') 
def end_timer(id):
    tasks[id].end_timer()
    return '', 204


@app.route('/api/task/store_result', methods=['POST']) 
def finished_task():
    request_data = json.loads(request.data)
    tasks[c.get_curr()].set_result(request_data['result'])
    tasks[c.get_curr()].set_backspaces(request_data['amount_back'])
    return '', 204


@app.route('/api/task/<int:id>/rating', methods=['POST']) 
def set_rating(id):
    request_data = json.loads(request.data)
    tasks[id].set_rating(request_data['index'], request_data['rating'])
    return '', 204

@app.route('/api/task/<int:id>/store') 
def store_task(id):
    d.store_task(tasks[id])
    d.store_ratings(tasks[id].ratings)
    return '', 204

@app.route('/api/survey_link')
def get_survey_link():
    return {'link': SURVEY_LINK}


#g.load_model()
print('Everything is ready')
app.run(debug=False)
