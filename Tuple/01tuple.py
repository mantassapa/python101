kort = (5,8,9,7,9,7) # kortezas skiresi nup saraso tuo kad jo turinys nekeiciams bei kortezas greiciau apdorojams
print(kort)
print(type(kort))
print(kort[1])
sar = [4,8,7]
sar[1]=15
print(sar)
# kort[1] = 15

persons = ('jonas', 'petraitis', 375827123213)
testas = (4,8)
tekstasA = 4, 8, 9 # tokiu budu irgi galima aprasyti korteza

print(type(tekstasA))
listA = list(tekstasA)
print(type(listA))

print(kort[1]+5)

x1,x2,x3,x4,x5,x6 = kort
print(type(x1))

sar1 = []
for i in range(len(kort)):
    sar1.append(kort[i]+i)

print(kort)
print(sar1)

print(kort.count(9))
print(kort.index(9))
kort +=(1,1,1)
print(kort)

kitasKort = kort
print(kitasKort)
print(id(kort))
print(id(kitasKort))


kort +=(1,1,1)
print(kort)
print(kitasKort)

aibeA = set()
print(aibeA)
