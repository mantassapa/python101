# Apskaiciuoti 100/sk
import math

veikia = True

while veikia:
    try:
        sk = int(input('iveskite skaiciu = '))
        rez = math.sqrt(100 / sk)
        veikia = False
    except ValueError as ex:
        print(f'Klaidos pranesimas {ex}. Kartokite ivedima')
    except ZeroDivisionError:
        print(f'Dalyba is 0 negalima.  kartokite...')
    except :
        print('ivyko nezinoma klaida')
    else: 
        print('panasu kad viskas gerai')
    finally: 
        print('man dzin ar viskas gerai ar blogai as vistiek veikiu')


print(f'sk = {sk}, rez = {rez}')