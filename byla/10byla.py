def valom():
    with open('10data.txt', 'w') as f:
        pass

def ivedimas(txt):
    sk = int(input(f'{txt} = '))
    return sk

def rasyti(txt):
    with open('10data.txt', 'a', encoding='utf-8') as f:
        f.write(f'{txt}\n')

valom()

kiek = ivedimas('kiek skaiciu sumuosime ')
rasyti(f'vartotojas ivede skaiciu {kiek}')

sum =0
list1=[]
for i in range(1, kiek+1):
    sk = ivedimas(f'sk{i}')
    rasyti(f'sk{i} = {sk}')
    sum += sk
    list1.append(sk)

print(f'suma = {sum}')
rasyti(f'suma = {sum}')