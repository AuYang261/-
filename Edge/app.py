from flask import Flask, request, render_template, make_response, session, redirect, url_for, jsonify
import config

app = Flask(__name__)
app.secret_key = b'auyang'

with app.app_context():
    # 加载配置文件
    app.config.from_object(config)

@app.route("/", methods=['GET', 'POST'])
def index():
    res = 'success!'
    return res

@app.route("/uploadFile", methods=['POST'])
def uploadFile():
    print(request.form)
    return request.form
    pass
