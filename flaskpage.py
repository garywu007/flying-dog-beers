import sys
from flask import Flask, request
from yattag import Doc

app = Flask(__name__)

@app.route('/')
def hello_world():
    cls1 = request.args.get('cls', default = '-', type = str)
    item = request.args.get('item', default = '-', type = str)
    
    doc, tag, text = Doc().tagtext()

    with tag('html'):
        with tag('head'):
            with tag('title'):
                text('i know what you think~~');
        with tag('body'):
            with tag('p', id = 'main'):
                text('your favourate ' + cls1 + ' is ' + item)

    result = doc.getvalue()
    return result

@app.route('/test/<first>/<second>')
def test_page(first, second):
    print(first)
    return 'your most favourate ' + first + ' is ' + second
