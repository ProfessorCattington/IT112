from flask import Flask, request, render_template
import random

app = Flask(__name__)

fortuneFormPath = 'HW3//fortuneForm.html'

@app.route("/")
def hello_world():
    return "<p> Hello! this is a basic web page! </p>"

@app.route("/about")
def about():
    return "<p>" \
    "<h1>About me</h1> \
        <br>My name is Mike. I am a student at NSC and currently taking web development courses. </br> \
        <br>I enjoy music, hiking and developing apps in python <br></p>"

@app.route("/fortune", methods = ['GET', 'POST'])
def fortune():
    if request.method == 'POST':
        name = request.form['user']
        color = request.form['color']
        number = request.form['number']

        userFortune, luckyNumber = getFortune(name, color, number)

        return render_template('fortuneTemplate.html', fortune=userFortune, luckyNumber=luckyNumber)
    else:
        return showFortunePage()

def showFortunePage():
    file = open(fortuneFormPath, 'r')
    webContent = file.read()
    return webContent

def getFortune(name, color, number):

    fortune = "Today " + name 

    if color == 'red' and (number == "1" or number == "3"):
        fortune += " will see an old friend."
    elif color == 'red' and (number == "2" or number == "4"):
        fortune += " will find a forgotten object."
    elif color == 'yellow':
        fortune += " will have a strange dream."
    elif color == 'green' and (number == "1" or number == "2"):
        fortune += " will have good luck!"
    elif color == 'green' and (number == "3" or number == "4"):
        fortune += " will be unlucky!"
    elif color == "blue":
        fortune += " will be inspired and try something new."

    luckyNumber = random.randint(1, 100)
    return (fortune, luckyNumber)

if __name__ == '__main__':
    app.run(debug=True)