# petriuko pazymiai 
# ivedamas pazimiu kiekis is suvedami pasymiai. rasti vidurki


kiek = int(input('kiek Pertriukas turi pazimiu....'))
p = []

for i in range(kiek):
    paz = int(input(f'iveskite {i+1}-aji pazimi...'))
    while not 0<paz<11:
        paz = int(input(f'blogais ivestas pazimys kartokite {i+1}-aji pazimi..'))
        
    p.append(paz)

print(f'Petriuko pazymiai {p}')

suma = 0
for i in p:
    suma+=i
vid = suma / len(p)
print(f'vidurkis..{vid}')
