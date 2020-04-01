import sys
from flask import Flask

app = Flask(__name__)

print("initial")

@app.route('/')
def hello_world():
    print("index")
    return 'Hello, World!'

@app.route('/test')
def test_page():
    print("/test")
    return 'In test page!'
