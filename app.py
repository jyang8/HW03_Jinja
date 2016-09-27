from flask import Flask, render_template
from utils import occupations

app = Flask(__name__) #create Flask object

@app.route("/")
def redirect():
    return "For more information, <a href='/occupations'>click here</a>."

@app.route("/occupations")
def tmplt():
    return render_template( 'occupations.html', collection = occupations.fullDict(), job = occupations.randOcc( occupations.dictCSV() ) )

if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
