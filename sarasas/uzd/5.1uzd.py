m = [5, 6, 1, 2, 8, 7, 14, 15, 2, 2, -85,-8, 13, 17,21,3]
sumalyg = 0
sumanelyg = 0
for i in m:
    if i>0:
        if i % 2 == 0:
            sumalyg +=1
        else:
            sumanelyg +=1
print(f'teigiamu nelyginiu elementu kiekis yra...{sumanelyg}')
