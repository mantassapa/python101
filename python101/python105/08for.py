#ivedame skaiciu 12 man atspausdina visus daliklius 1, 2, 3, 4, 6
skaicius = int(input('iveskite skaiciu: '))
kiek = 0
for i in range(1, skaicius):
    if skaicius%i == 0 and skaicius != i :
        dal = i
        kiek = kiek+1
        print (f'dalikliai: {i}, dalikliu yra {kiek}')