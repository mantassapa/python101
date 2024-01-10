# 5. 18.Sugeneruokite atsitiktini dvimatįmasyvą A[n][m], kuriame n ir m yra atsitiktiniai skaičiai iš intervalo [10; 30],
# o masyvo elementai yra atsitiktiniai skaičiai iš intervalo [-100; 100]. Išsaugokite šį masyvą byloje. 
# Sugeneruokite atsitiktinį skaičių sk iš intervalo [-100; 100].Patikrinkite, ar sugeneruotas skaičius sk yra masyvo A elementas. 
# Jei yra –atspausdinkite jo eilutės ir stulpelio numerį (vietą). Gali būti taip, kad elementas yra pasikartojanti, tuomet atspausdinkite visas jo vietas.s




import random
A = []
n = random.randint(10, 30)
m = random.randint(10, 30)
for i in range(n*m):
    s = random.randint(-100, 100)
    A.append(s)
with open('data01.txt', 'w') as f:
    t = str(A)
    txt = t[1:-1]
    f.write(txt)


def readFile():
    n1= n
    m1 =m
    with open('data01.txt', 'r') as f:
        arrayTxt = f.read().split(', ')
        arrayInt = [int(i) for i in arrayTxt]
        p = 0
        g = m1
        duMas = []
        for i in range(n1):
            duMas.append(arrayInt[p:g])
            p = g
            g += m1
        return duMas

def result():
    duList = readFile()
    with open('data01.txt', 'w') as f:
        for n in duList:
            t = str(n)
            txt = t[1:-1].replace(', ', '\t')
            f.write(f'{txt}\n')

result()
sk = random.randint(-100, 100)

columnNr = A.index(sk)-m
rowNr = A.index(sk)//n

if A.index(sk):
    print(f"indexas={A.index(sk)}, skaicius = {sk}, columns={m}, rows={n} column{columnNr} row{rowNr}")
else:print('tokio skaiciaus nera dvimetiame masyve')
