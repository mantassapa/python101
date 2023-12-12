# w, r, a, w+, r+
#vbyloje nprime irasyti 3 skaicis, nuskaityti ir susumuoti ir pabaigoje irasyti
#r+ papilto faila (negalis sukurti failo)
#w+ peraso faila (sukuria faila)
def viskas (txt):
    with open('09data.txt', 'w+') as f:
        f.write('5\n')
        f.write('15\n')
        f.write('20\n')
        f.seek(0)
        sk1 = int(f.readline())
        sk2 = int(f.readline())
        sk3 = int(f.readline())
        s = sk1 + sk2 + sk3
        f.write(txt + '\n')
        f.write(f'{sk1} + {sk2} + {sk3} = {s}\n')

    for i in range(1,6):
        viskas(f'rezultatas Nr. {i}')
