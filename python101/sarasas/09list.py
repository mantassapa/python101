# petriuko, Antano, Stasio.... pazymiai 
# ivedamas pazimiu kiekis is suvedami pasymiai. rasti vidurki
# sukurti masyva mamai (tik teigiami) 4 ir didesni ir apskaiciuoti vidurki
# sukurti masyva teciui (tik teigiami) 6 ir didesni ir apskaiciuoti vidurki
MAMA = 4
TATA = 6
#-----------------funkcija grazinanti pazimiu kieki----------
def kiekis(vardas):
    kiek = int(input(f'kiek {vardas} turi pazimiu....'))
    return kiek
#-------------------------------------------------------------
#----------------funkcija pazymiams ivesti ir grazinti-------
def ivedimas(kiek, vardas):
    p = []
    i = 1
    while i <=kiek:
        paz = int(input(f'iveskite {vardas} {i}-aji pazimi...'))
        if 1<=paz<=10:
            p.append(paz)
            i += 1
        else:
            print(f'Pazimys {paz} neegzistuoja, kartokite ivedima')
    return p
#------------------------------------------------------------
#------------------funkcija apskaiciuoja ir grazina vidurki---
def vidurkis(p):
    if len(p)>0:
        vid = sum(p) / len(p)
    else:
        vid = 0
    return vid
#------------------------------------------------------------
#-------------------sarasas tevams---------------------------
def tevams(p, kriterijus):
    pTev = []
    for i in p:
        if i >= kriterijus:
            pTev.append(i)
    return pTev
#------------------------------------------------------------
#-----------------funkcija duomenu isvedimui----------------
def isvedimas(vardas):
    # paz = ivedimas(kiekis(vardas), vardas)
    # vidMok = vidurkis(paz)
    # pazMama = tevams(paz, MAMA)
    # pazTetis = tevams(paz, TATA)
    # vidMama = vidurkis(pazMama)
    # vidTetis = vidurkis(pazTetis)
    # print(f'{vardas} pazymiai {paz} vidurkis {vidMok}')
    # print(f'{vardas} Mamos pazymiai {pazMama} vidurkis {vidMama}')
    # print(f'{vardas} Tecio pazymiai {pazTetis} vidurkis {vidTetis}')

    paz = ivedimas(kiekis(vardas), vardas)
    pazMama = tevams(paz, MAMA)
    pazTetis = tevams(paz, TATA)
    print(f'{vardas} pazymiai {paz} vidurkis {vidurkis(paz)}')
    print(f'{vardas} Mamos pazymiai {pazMama} vidurkis {vidurkis(pazMama)}')
    print(f'{vardas} Tecio pazymiai {pazTetis} vidurkis {vidurkis(pazTetis)}')
#----------------------------------------------------------
klase = ['Petras', 'Antanas', 'Stasys', 'Rimas', 'Jonas']
for i in klase:
    isvedimas(i)

# isvedimas('Petras')
# isvedimas('Antanas')
# isvedimas('Stasys')




