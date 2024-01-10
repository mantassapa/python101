# petriuko pazymiai 
# ivedamas pazimiu kiekis is suvedami pasymiai. rasti vidurki
# sukurti masyva mamai (tik teigiami) 4 ir didesni ir apskaiciuoti vidurki
# sukurti masyva teciui (tik teigiami) 6 ir didesni ir apskaiciuoti vidurki


kiek = int(input('kiek Pertriukas turi pazimiu....'))
p = []
pm = []
pt = []
i = 1

while i <=kiek:
    paz = int(input(f'iveskite {i}-aji pazimi...'))
    if 1<=paz<=10:
        p.append(paz)
        i += 1
    else:
        print(f'Pazimys {paz} neegzistuoja, kartokite ivedima')


print(f'Petriuko pazymiai {p}')
print(f'mamai pazymiai{pm}')

suma = 0
for i in p:
    suma+=i
vid = suma / len(p)
print(f'vidurkis..{vid}')
