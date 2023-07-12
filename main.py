import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    confText = sys.argv[1] if len(sys.argv) > 1 else 'No parameter provided'
    html = f'<h1>{text}</h1>'
    return html

if __name__ == '__main__':
    confPort = sys.argv[2] if len(sys.argv) > 2 else 'No parameter provided'
    app.run(host='0.0.0.0', port=confPort)