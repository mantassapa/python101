import random


def loop():
    n = int(input('n=...'))
    sk1 = random.randrange(n)
    sk = 0
    while sk != sk1:
        for i in range(1, n):
            sk = int(input('spekite skaiciu...'))
            if sk == sk1:
                print(f'seikiname atspejote,.. jus spejote {i} kart')
                quest = input('norite zaisti dar karta (taip/ne)..')
                if quest == 'taip':
                    continue
                elif quest == 'ne':
                    break
                else:
                    print('iveskite (taip/ne)')
            elif sk < sk1:
                if sk < 0:
                    print('visai ne i tema')
                else:
                    print('jusu skaicius yra mazesnis')
            elif sk > sk1:
                if sk > n:
                    print('visai ne i tema')
                else:
                    print('jusu skaicius yra didesnis')


loop()
