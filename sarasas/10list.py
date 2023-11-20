#duotas sarasas m = [5,8,8,5,7,4,1,1,'labas',5,8,-7,-7,'labas']
#atspasudinti kiek kiekvieno elemetu yra
#pvz 5 yra 2
#   8 yra 3
#   7 yra 1
#   4 yra 1
#   1 yra 2
#   labas yra 2
#   -7 yra 2
#negalima naudoti dict, set!!!!!
m = [5, 8, 8, 5, 7, 4, 1, 1, 'labas', 5, 8, -7, -7, 'labas']
rep = []
for i in m:
    if not(i in rep):
        rep.append(i)
for i in rep:
    print(f'{i} yra {m.count(i)}')
