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
def gen_checkerboard(x= 8, y= 8, color1= "red", color2= "black"):
    return render_template("index.html", x= x, y= y, color1= color1, color2= color2)

@app.route('/r')
def random_board():

    #random coordinate for x,y
    c = lambda : round(random.random()*(20-1) + 1)

    #random rgb sub value (i.e. rgb(r,r,r))
    r = lambda : (round(random.random()*255 - 0))

    #generate string to pass as CSS background-color property
    color1 = f"rgb({r()}, {r()}, {r()})"
    color2 = f"rgb({r()}, {r()}, {r()})"

    return render_template("index.html", x= c(), y= c(), color1= color1, color2= color2)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.