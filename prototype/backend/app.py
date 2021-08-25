from flask import Flask, request, json
from pyfiles.generator import Generator
from pyfiles.taskmanager import tasks, fill_tasks, Current
from pyfiles.datawriter import DataWriter
from pyfiles.ratings import questions
from pyfiles.constants import SURVEY_LINK, AMOUNT_SUGGESTIONS

app = Flask(__name__)

d = DataWriter()
g = Generator()
c = Current()


@app.route('/api/generate', methods=['POST'])
def generate_sentence():
    request_data = json.loads(request.data)
    sentence = request_data['content']

    if c.get_curr() != None:
        tasks[c.get_curr()].start_timer()

    index = len(sentence.split(' '))
    sen, t = g.generate_sentence(sentence)
    if c.get_curr() != None:
        tasks[c.get_curr()].add_generating_time(t)

    return {'sentence': sen,
            'index': index}


@app.route('/api/generate_options', methods=['POST'])
def generate_options():
    request_data = json.loads(request.data)
    pre = request_data['pre_sentence']

    if c.get_curr() != None:
        tasks[c.get_curr()].start_timer()
        tasks[c.get_curr()].log(pre)

    sen, t = g.generate_multiple_options(pre, AMOUNT_SUGGESTIONS)
    if c.get_curr() != None:
        tasks[c.get_curr()].add_generating_time(t)

    return {'sentences': sen}


@app.route('/api/user/<int:uid>') 
def set_user_id(uid):
    fill_tasks(uid)
    d.set_user_id(uid)
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
    if c.get_curr() != None:
        tasks[c.get_curr()].set_result(request_data['result'])
    return '', 204


@app.route('/api/task/log_input', methods=['POST'])
def log_input():
    request_data = json.loads(request.data)
    if c.get_curr() != None:
        tasks[c.get_curr()].start_timer()
        tasks[c.get_curr()].log(request_data['sentence'])
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
    d.write_log(tasks[id].id, tasks[id].logger.get_log())
    c.not_active()
    return '', 204


@app.route('/api/survey_link')
def get_survey_link():
    return {'link': SURVEY_LINK}


g.load_model()
app.run(debug=False)