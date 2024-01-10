# ivedu sav diena skaitiumi man atspausdina pavad

diena = int(input('kokia sav diena'))
viskasok = True
match diena:
    case 1:
        txt = 'Pirmadienis'
    case 2:
        txt = 'Antradienis'
    case 3:
        txt = 'Treciadienis'
    case 4:
        txt = 'ketvirtadienis'
    case 5:
        txt = 'penktadienis'
    case 6:
        txt = 'sestadienis'
    case 7:
        txt = 'sekmadienis'
    case _:
        print('blogai ivesti duomenys') #txt = 'blogai ivesti duomenys'
        viskasok = False

if viskasok :
    print(f'{diena} - {txt}')
