kiek = 0
for i in range(1000, 10000):
    sk1 = i//1000
    sk2 = i//100%10
    sk3 = i//10%10
    sk4 = i%10
    suma = (sk1+sk2+sk3+sk4)^2
    daug = sk1*sk2*sk3*sk4
    if suma == daug :
        print(i, end=(', '))
        kiek +=1
print(f'tokiu skaiciu yra {kiek}')