# sugeneruoti atsitiktini masyvo eiluciu ir stulpeliu kieki ir reziu nuo 5
#sugeneruoti dvimati masyva ir ji issaugoti duomenis byloje [-100; 100]
#nuskaityti duomenis
#rez bylos sukutimas ???
import random

def duomenuFailas():
    row= random.randint(5,25)
    col= random.randint(5,25)
    listsk = []
    for i in range(row*col):
        sk = random.randint(-100,100)
        listsk.append(sk)
    with open('data.txt', 'w') as f:
        t=str(listsk)
        txt= t[1:-1]
        f.write(txt)
    return row, col

def skaitomfaila():
    row, col = duomenuFailas()
    with open('data.txt', 'r') as f:
        listTxt = f.read().split(', ')
        listInt = [int(i) for i in listTxt]
        p = 0
        g = col
        duMas = []
        for i in range(row):
            duMas.append(listInt[p:g])
            p = g
            g+= col
        return duMas
    
print(skaitomfaila())

def rezultatas():
    duList = skaitomfaila()
    with open('rez.txt', 'w')as f:
        for row in duList:
            t = str(row)
            txt = t[1:-1]
            txt1 = txt.replace(', ', '\t') # \t - tobuliatorius
            f.write(f'{txt1}\n')