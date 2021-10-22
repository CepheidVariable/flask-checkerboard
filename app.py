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
def get_checkerboard(x= 8, y= 8, color1= "red", color2= "black"):
    return render_template("index.html", x= x, y= y, color1= color1, color2= color2)

@app.route('/r')
def get_random_checkerboard():

    #random coordinate for x,y
    def _get_coord(): return round(random.random()*(20-1) + 1)

    #random sub-value(x) for rgb color (i.e. rgb(x,x,x))
    def _get_rgb(): return round(random.random()*255 - 0)

    #generate string to pass as CSS background-color property
    color1 = f"rgb({_get_rgb()}, {_get_rgb()}, {_get_rgb()})"
    color2 = f"rgb({_get_rgb()}, {_get_rgb()}, {_get_rgb()})"

    return render_template("index.html", x= _get_coord(), y= _get_coord(), color1= color1, color2= color2)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.