# ivedamas kaicius rasti to skaiciaus skaitmenu suma..
def sumavimas(sk):
    suma=0
    while sk > 0:
        x1 = sk % 10
        sk = sk // 10 # sk //= 10
        suma+=x1
    return(suma)
sk = int(input('ivedame skaiciu...'))
s = sumavimas(sk)

print(f'skaiciaus {sk} skaitmenu suma = {s}')