from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello! this is a basic web page! </p>"

@app.route("/about")
def about():
    return "<p>" \
    "<h1>About me</h1> \
        <br>My name is Mike. I am a student at NSC and currently taking web development courses. </br> \
        <br>I enjoy music, hiking and developing apps in python <br></p>"