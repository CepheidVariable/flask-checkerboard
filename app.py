from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.errorhandler(Exception)
def errorhandler(err):
    app.logger.exception(err)
    return "You typed a bad route."

@app.route('/')
@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>/<int:y>/<color1>')
@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def gen_checkerboard(x= 8, y= 8, color1= "255,0,0", color2= "0,0,0"):
    return render_template("index.html", x= x, y= y, color1= color1, color2= color2)

@app.route('/r')
def random_board():
    x= random.random()*(20-1) + 1
    y= random.random()*(20-1) + 1
    color1= ""
    color2= ""

    for i in range(3):
        color1 += str(round(random.random()*255 - 0)) + ","
        color2 += str(round(random.random()*255 - 0)) + ","
    color1 = color1[:-1]
    color2 = color2[:-1]

    return render_template("index.html", x= int(x), y= int(y), color1= color1, color2= color2)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.