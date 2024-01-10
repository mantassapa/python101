# sugeneruoti atsitiktini masyvo eiluciu ir stulpeliu kieki ir reziu nuo 5
#sugeneruoti dvimati masyva ir ji issaugoti duomenis byloje [-100; 100]
#nuskaityti duomenis
import random

def gautiDvimatiSarasa():
    row= random.randint(5,25)
    col= random.randint(5,25)
    DuMas = []
    for i in range(row*col):
        eil=[]
        for j in range(col):
            eil.append(random.randint(-100,100))
    return DuMas

def rezultatas():
    duList = gautiDvimatiSarasa()
    with open('rez3.txt', 'w')as f:
        for row in duList:
            t = str(row)
            txt = t[1:-1]
            txt1 = txt.replace(', ', '\t') # \t - tobuliatorius
            f.write(f'{txt1}\n')