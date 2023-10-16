def ivedimas(kelintas):
    p = int(input(f'Iveskite petriuko {kelintas}-aji pazymi...'))
    geras = 1<=p<=10
    if not(geras) :
            print('blogai ivestas pazymys') 
            return ivedimas(kelintas)
    else:

            return p 




kiek = int(input('kiek Petriukas turi pazymiu...'))
for i in range(1, kiek+1):
    paz = ivedimas(i)
    if i == 1:
        did = paz
        vieta = 1
    elif paz > did:
        did = paz
        vieta = i
    




    
print (f'petriuko didziausias pazymys {did}, jo vieta {i}')