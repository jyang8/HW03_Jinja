import random, csv

#builds dictionary from csv file
def fullDict():
    d = {}
    with open('data/occupations.csv') as data:
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
