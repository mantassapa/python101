# Apskaiciuoti 100/sk
import math

veikia = True

while veikia:
    try:
        sk = int(input('iveskite skaiciu = '))
        rez = math.sqrt(100 / sk)
        veikia = False
    except :
        print('ivyko kazkokia klaida, kartokite')
    else: 
        print('panasu kad viskas gerai')


print(f'sk = {sk}, rez = {rez}')