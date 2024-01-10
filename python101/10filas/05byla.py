def sukurtBylas(failas, tekstas):
    with open(failas, 'w', encoding='utf-8') as f:
        f.write(tekstas)
 

def nuskaitoBylas(failas):
    with open(failas, 'r', encoding='utf-8') as f:
        txt = f.read()
        return txt

for i in range(1,6):
    sukurtBylas(f'{i}byla.txt', f'{i} byloje irasyta informacija')
    print(nuskaitoBylas(f'{i}byla.txt'))