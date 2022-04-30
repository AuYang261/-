from flask import Flask, request, render_template, make_response, session, redirect, url_for, jsonify
import config
import os

app = Flask(__name__)
app.secret_key = b'auyang'

with app.app_context():
    # 加载配置文件
    app.config.from_object(config)

@app.route("/", methods=['GET', 'POST'])
def index():
    request.form
    res = 'success!'
    return res

@app.route("/uploadFile", methods=['POST'])
def uploadFile():
    if not os.path.exists('../userFiles'):
        os.mkdir('../userFiles')
    request.files['file'].save('../userFiles/' + request.files.get('file').filename)
    return redirect('http://127.0.0.1:5001')
    pass
