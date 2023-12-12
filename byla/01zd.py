import random
 
def rasyti(txt):
    with open('reg.txt', 'a', encoding='utf-8') as f:
        f.write(f'{txt}\n') 

def zaidimas():
    zaidimas.kartai+=1
    n = int(input('Iveskite maksimalu skaiciu n:... '))
    rasyti(f'Iveskite maksimalu skaiciu n:... {n}')
    if n <= 0:
      print('Ivestas netinkamas skaicius, iveskite nauja:...')
      rasyti(f'Ivestas netinkamas skaicius, iveskite nauja:...{n}')
      return
    sk = random.randint(1, n)
    spejimai = 0
    while True:
        spejimas = int(input(f'Atspekite mano skaiciu nuo 1 iki {n}:... '))
        spejimai += 1
        rasyti(f'Atspekite mano skaiciu nuo 1 iki {n}:... ')
        if spejimas < 1 or spejimas > n: print(f'Spejimas turi būti nuo 1 iki {n}.'),rasyti(f'Spejimas turi būti nuo 1 iki {n}.')
        elif spejimas < sk: print(f'mano skaicius didesnis uz {spejimas}.'),rasyti(f'mano skaicius didesnis uz {spejimas}.')
        elif spejimas > sk: print(f'mano skaicius mazesnis uz {spejimas}.'),rasyti(f'mano skaicius mazesnis uz {spejimas}.')
        else:
            print(f'Sveikiname! Atspejot skaiciu {sk} per {spejimai} spejimus.')
            rasyti(f'Sveikiname! Atspejot skaiciu {sk} per {spejimai} spejimus.')
            break
    kartot = input('Ar norite zaisti dar karta? (t/n): ')
    rasyti(f' i uzklausa Ar norite zaisti dar karta? vartotojas pasirinko taip {kartot}' )
    if kartot == 't':zaidimas()
    else: print(f'Aciu, kad zaidet! '),rasyti(f'Aciu, kad zaidet!, vartotojas ziade {zaidimas.kartai} kart')
zaidimas.kartai = 0

zaidimas()
