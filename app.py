import os
from flask import Flask

app = Flask(__name__)

app_text = os.environ['APP_TEXT']


@app.route('/')
def index():
    html = f'<h1>hello {app_text}</h1>'
    return html
