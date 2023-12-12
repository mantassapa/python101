import random
 
def rasyti(txt):
    with open('reg.txt', 'a', encoding='utf-8') as f:
        f.write(f'{txt}\n') 

def zaidimas():
    zaidimas.kartai+=1
    Nr1 = input('iveskite varta pirmo ziadejo...')
    Nr2 =input('iveskite varta antro ziadejo...')
    l = int(input('Iveskite lazdeliu skaiciu... '))
    rasyti(f'Zaideju vardai: {Nr1} ir {Nr2}')
    rasyti(f'Lazdeliu pasirinktas skaicius yra {l}')
    print(f'Lazdeliu pasirinktas skaicius yra {l}')
    if l <= 0:
      print('Ivestas netinkamas skaicius, kartokite:...')
      return
    eil = random.randint(1, 2)
    if eil == 1:
        print(f'zaidima pradeda {Nr1}')
        rasyti(f'zaidima pradeda {Nr1}')
        while l>0:
            sk= int(input(f'{Nr1} kiek norite paimti lazdeliu... '))
            if sk < 1 or sk > l: print(f'lazdeliu skaicius turi būti nuo 1 iki {l}.')
            else:
                l-=sk
                print(f'{Nr1} paima {sk} lazdeles. Liko {l}')
                rasyti(f'{Nr1} paima {sk} lazdeles. Liko {l}')
                if l==0:
                    print(f' laiejo zaidma {Nr2}')
                    rasyti(f' laiejo zaidma {Nr2}')
                    break
            sk= int(input(f'{Nr2} kiek norite paimti lazdeliu... '))
            if sk < 1 or sk > l: print(f'lazdeliu skaicius turi būti nuo 1 iki {l}.')
            else:
                l-=sk
                print(f'{Nr2} paima {sk} lazdeles. Liko {l}')
                rasyti(f'{Nr2} paima {sk} lazdeles. Liko {l}')
                if l==0:
                    print(f' laimejo zaidima {Nr1}')
                    rasyti(f' laimejo zaidima {Nr1}')
                    break

    else:
        print(f'zaidima pradeda {Nr2}')
        rasyti(f'zaidima pradeda {Nr2}')
        while l>0:
            sk= int(input(f'{Nr2} kiek norite paimti lazdeliu... '))
            if sk < 1 or sk > l: print(f'lazdeliu skaicius turi būti nuo 1 iki {l}.')
            else:
                l-=sk
                print(f'{Nr2} paima {sk} lazdeles. Liko {l}')
                rasyti(f'{Nr2} paima {sk} lazdeles. Liko {l}')
                if l==0:
                    print(f' laiejo zaidma {Nr1}')
                    rasyti(f' laiejo zaidma {Nr1}')
                    break
            sk= int(input(f'{Nr1} kiek norite paimti lazdeliu... '))
            if sk < 1 or sk > l: print(f'lazdeliu skaicius turi būti nuo 1 iki {l}.')
            else:
                l-=sk
                print(f'{Nr1} paima {sk} lazdeles. Liko {l}')
                rasyti(f'{Nr1} paima {sk} lazdeles. Liko {l}')
                if l==0:
                    print(f' laimejo zaidima {Nr2}')
                    rasyti(f' laimejo zaidima {Nr2}')
                    break
        
    kartot = input('Ar norite zaisti dar karta? (t/n): ')
    if kartot == 't':zaidimas()
    else: 
        print(f'Aciu, kad zaidet!')
        rasyti("Į užklausą „Ar žaisite dar“ pasirinko „Ne“")
        print(f'Žaidimąžaidė {zaidimas.kartai} kartą(us)')
        rasyti(f'Žaidimąžaidė {zaidimas.kartai} kartą(us)')

zaidimas.kartai = 0

zaidimas()
