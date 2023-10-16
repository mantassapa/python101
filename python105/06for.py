from itertools import count
kiek = int(input('kiek Petriukas turi pazymiu...'))
suma = 0
for i in range(1, kiek+1):
    p = int(input(f'Iveskite petriuko {i}-aji pazymi...'))
    geras = 1<=p<=10
    if not (geras) :
        for j in count(0):
            print('blogai ivestas pazymys') 
            p = int(input(f'Iveskite petriuko {i}-aji pazymi...'))
            if 1<=p<=10:
                break

    suma = suma + p


    
vid = suma / kiek
print (f'petriuko vidurkis {vid}')