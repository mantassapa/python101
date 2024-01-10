def sukurtif():
    with open('03data.txt', mode='w', encoding='utf-8') as f:
        f.write('10, 15, -25, 45, 65, 89, 16, 18, 20\n')
        f.write('15, 36, 41, 55, 47\n')
        
def nuskaitytif():
    with open('03data.txt', 'r', encoding='utf-8') as f:
        eil1 = f.readline().split(', ')
        eil2 = f.readline().split(', ')
        eil1int = [int(x) for x in eil1]
        eil2int = [int(x) for x in eil2]
    return eil1int, eil2int

def isaugotiduomen(failas, duom):
    with open(failas, 'w', encoding='utf-8') as f:
        txtduom = str(duom)
        f.write(txtduom[1:-1])

sukurtif()
list1, list2 = nuskaitytif()
print(list1)
listnew = [i for i in list1 if i%2 == 0]
print(listnew)

isaugotiduomen('03rez.txt', listnew)