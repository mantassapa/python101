# ivedami du skaiciai. did priskiremi didziausi o maz maziausi
# nenaudoti min ir max funkciju
a = int(input('a=...'))
b = int(input('b=...'))

if a > b:
    did = a
    maz = b
    print(f'{did} yra didesnis uz {maz}')
elif a < b:
    did = b
    maz = a
    print(f'{did} yra didesnis uz {maz}')
else:
    print(f'{a} lygus {b}')

