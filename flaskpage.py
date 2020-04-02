import sys
from flask import Flask

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
def hello_world():
    cls1 = request.GET.get('cls')
    item = request.GET.get('item')
    
    t = Template(index_html)
    c = Context({"class": cls1, "item":item})
    return t.render(c)

@app.route('/test')
def test_page():
    print("/test")
    return 'In test page!'
