# Apskaiciuoti 100/sk
import math

while True:
    try:
        sk = int(input('iveskite skaiciu = '))
        rez = math.sqrt(100 / sk)
        break
    except ValueError as ex:
        print(f'Klaidos pranesimas {ex}. Kartokite ivedima')
    except ZeroDivisionError:
        print(f'Dalyba is 0 negalima.  kartokite...')
    except :
        print('ivyko nezinoma klaida')
    else:
        print('panasu kad viskas gerai')


print(f'sk = {sk}, rez = {rez}')