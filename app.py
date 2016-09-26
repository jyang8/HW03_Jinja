from flask import Flask, render_template
import random, csv

#------------------------Choosing a random occupation------------------------

#builds dictionary from csv file
def fullDict():
    d = {}
    with open('occupations.csv') as data:
        reader = csv.DictReader(data)
        for row in reader:
            occ = row['Job Class']
            percent = float(row['Percentage'])
            d[occ] = percent
    return d

#builds dictionary from csv file, without extraneous info
def dictCSV():
    d = fullDict()
    del d['Total']
    return d

#returns a randomly selected occupation where the results are weighted by the percentage given
def randOcc(d):
    randVal = random.random()*99.8
    ctr = 0.0
    for job in d:
        percent = d[job]
        if randVal < ctr + percent:
            return job
        else:
            ctr += percent

#print fullDict()
        
#----------------------------------------------------------------------------

app = Flask(__name__) #create Flask object

@app.route("/")
def redirect():
    return "For more information, <a href='/occupations'>click here</a>."

@app.route("/occupations")
def tmplt():
    return render_template( 'occupations.html', foo = "Job Selection", collection = fullDict(), job = randOcc( dictCSV() ) )

if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    #app.debug = True 
    app.run()
