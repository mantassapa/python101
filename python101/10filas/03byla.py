def sukurtif():
    with open('03data.txt', mode='w', encoding='utf=8') as f:
        f.write('10 15 -25 45 65 89\n')
        f.write('15 36 41 55 47\n')
        
def nuskaitytif():
    with open('03data.txt', 'r', encoding='utf=8') as f:
        eil1 = f.readline()
        eil2 = f.readline()
        print(f.closed)
        print(type(eil1))
    print(f.closed)

sukurtif()
nuskaitytif()