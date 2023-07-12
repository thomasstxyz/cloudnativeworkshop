import os
from flask import Flask

app = Flask(__name__)

app_text = os.environ['APP_TEXT']
app_port = os.environ['APP_PORT']


@app.route('/')
def index():
    html = f'<h1>{app_text}</h1>'
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app_port)
