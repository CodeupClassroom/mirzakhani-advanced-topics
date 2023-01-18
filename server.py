from flask import Flask
from flask import render_template
from flask import request
from model import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model-input')
def render_model():
    return render_template('model-input.html')

@app.route('/model', methods=['POST'])
def handle_model():
    msg = request.form['msg']
    return render_template('model-result.html', msg=predict(msg))