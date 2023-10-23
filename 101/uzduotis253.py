def ivedimas(balas):
    x = int(input(f'iveskite pirmo {balas} bala...'))
    geras = x == 0 or x == 1
    if not (geras):
        print('blogas suvedimas')
        return ivedimas(balas)
    else:
        return x


def ivedimas2(balas):
    x1 = 1
    geras = x1 == 0 or x1 == 1
    if not (geras):
        print('blogas suvedimas')
        return ivedimas2(balas)
    else:
        return x1

for a in range(1, 6):
    al = ivedimas(a)
    if a == 1:
        a = a1 = 10
        a = a2 = 20
        a = a3 = 30
        a = a4 = 40
        a = a5 = 50
    else:
        a = a11 = 0
        a = a21 = 0
        a = a31 = 0
        a = a41 = 0
        a = a51 = 0


suma = 0
suma1 = a1 + a2 + a3 + a4 + a5 + 50
suma2 = a1 + a21 + a31 + a41 + a5 + 20
suma3 = a1 + a21 + a3 + a4 + a51  - 30
suma4 = a11 + a2 + a3 + a4 + a51  - 40
suma5 = a11 + a21 + a31 + a4 + a5 // 2
suma6 = 0

print(f'..{suma1}..{suma2}..{suma3}..{suma4}..{suma5}')

if suma1:
    print('false')
elif suma2:
    print('no')
else:
    print('why tho')

for b in range(1, 6):
    b1 = ivedimas2(b)
