# 5. 18.Sugeneruokite atsitiktini dvimatįmasyvą A[n][m], kuriame n ir m yra atsitiktiniai skaičiai iš intervalo [10; 30],
# o masyvo elementai yra atsitiktiniai skaičiai iš intervalo [-100; 100]. Išsaugokite šį masyvą byloje. 
# Sugeneruokite atsitiktinį skaičių skiš intervalo [-100; 100].Patikrinkite, ar sugeneruotas skaičius skyra masyvo A elementas. 
# Jei yra –atspausdinkite jo eilutės ir stulpelio numerį (vietą). Gali būti taip, kad elementas yra pasikartojanti, tuomet atspausdinkite visas jo vietas.s



#Sugeneruoti atsitiktini masyvo eiluciu ir stulpeliu kieki is reziu nuo 5 iki 25
#Sugeneruoti dvimati masyva ir ji issaugoti duomenis byloje [-100; 100]
#Nuskaityti duomenis
#rez bylos suskurimas ???
import random
 
def duomenuFailas():
    row = random.randint(5, 25)
    col = random.randint(5, 25)
    # print(f'{row}, {col}')
    listsk = []
    for i in range(row*col):
        sk = random.randint(-100, 100)
        listsk.append(sk)
    with open('data.txt', 'w') as f:
        t = str(listsk)
        txt = t[1:-1]
        f.write(txt)
    return row, col
 
def skaitomFaila():
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
            g += col
        return duMas
 
def rezultatas():
    duList = skaitomFaila()
    with open('rez.txt', 'w') as f:
        for row in duList:
            t = str(row)
            txt = t[1:-1].replace(', ', '\t')
            # txt1 = txt.replace(', ', '\t')
            f.write(f'{txt}\n')
 
   
 
rezultatas()



#Sugeneruoti atsitiktini masyvo eiluciu ir stulpeliu kieki is reziu nuo 5 iki 25
#Sugeneruoti dvimati masyva ir ji issaugoti duomenis byloje [-100; 100]
#rez bylos suskurimas ???
# import random
 
# def gautiDvimatiSarasa():
#     row = random.randint(5, 25)
#     col = random.randint(5, 25)
#     duMas= []
#     for i in range(row):
#         eil = []
#         for j in range(col):
#             eil.append(random.randint(-100, 100))
#         duMas.append(eil)
#     return duMas
 
 
 
# def rezultatas():
#     duList = gautiDvimatiSarasa()
#     # print(duList)
#     with open('rez3.txt', 'w') as f:
#         for row in duList:
#             t = str(row)
#             txt = t[1:-1].replace(', ', '\t')
#             # txt1 = txt.replace(', ', '\t')
#             f.write(f'{txt}\n')
 
# def skaiciavimai():
#     pass
 
   
 
# rezultatas()



