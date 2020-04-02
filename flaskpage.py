import sys
from flask import Flask, request
from yattag import Doc

app = Flask(__name__)

index_html = """
<html>
<head>
<title>i know what's your favourate {{ class }}</title>
</head>
<body>
your favourate {{ class }} is {{item}}
</body>
</html>
"""
doc, tag, text = Doc().tagtext()

with tag('html'):
    with tag('body'):
        with tag('p', id = 'main'):
            text('some text')
        with tag('a', href='/my-url'):
            text('some link')

result = doc.getvalue()

@app.route('/')
def hello_world():
    cls1 = request.args.get('cls', default = '-', type = str)
    item = request.args.get('item', default = '-', type = str)
    
    doc, tag, text = Doc().tagtext()

    with tag('html'):
        with tag('body'):
        with tag('body'):
            with tag('p', id = 'main'):
                text('your favourate ' + cls1 + ' is ' + item)

    result = doc.getvalue()
    return result

@app.route('/test')
def test_page():
    print("/test")
    return 'In test page!'
