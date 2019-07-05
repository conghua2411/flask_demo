from flask import Flask, request, json

from mongoTest import getData, getDataPosts

app = Flask(__name__)


def runServer():
    app.run(debug=True)


@app.route("/")
@app.route("/home")
def home():
    return "hello world!"


@app.route("/wtf", methods=['GET', 'POST'])
def wtf():
    data = request.args.get('name')
    print(data)
    return "<h1>wtf name : - %s</h1>" % data


@app.route("/testPost", methods=['POST'])
def testPost():
    name = request.form['name']
    age = request.form['age']

    data = {'name': name, 'age': age, 'wtf': "wtf bro"}

    return json.dumps(data)


@app.route("/getId", methods=['GET'])
def getId():
    data = getData(request.args.get('id')).limit(10)
    array = []
    for x in data:
        array.append(json.dumps(x))

    return json.dumps(array)


def setupDataComment(comments):
    text = ""
    for comment in comments:
        text += "<li>"
        text += comment['author'] + "<br>"
        text += comment['body'] + "<br>"
        text += "</li>"
    return text


def setupDataPost(post):
    text = ""
    text += "id: %s<br>" % post['_id']
    text += "author: %s<br>" % post['author']
    text += "<br>%s<br><br>" % post['body']
    text += "<ul>"
    text += setupDataComment(post['comments'])
    text += "</ul><br><br>"
    return text


@app.route("/getPosts", methods=['GET'])
def getPosts():
    data = getDataPosts().limit(10)
    text = "<ol>"
    for x in data:
        x['_id'] = str(x['_id'])
        text += "<li>"
        text += setupDataPost(x)
        text += "</li>"
    text += "</ol>"
    return text
