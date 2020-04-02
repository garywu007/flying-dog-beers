import sys
from flask import Flask
from django.template import Template, Context

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

@app.route('/')
def hello_world(self):
    cls1 = self.request.get('cls')
    item = self.request.get('item')
    
    t = Template(index_html)
    c = Context({"class": cls1, "item":item})
    return t.render(c)

@app.route('/test')
def test_page():
    print("/test")
    return 'In test page!'
