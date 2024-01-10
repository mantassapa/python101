# ivedu sav diena skaitiumi patikrinti ar tai darbo diena ar savaitgalis

diena = int(input('kokia sav diena'))
viskasok = True
match diena:
    case 1 | 2 | 3 | 4 | 5:
        txt = 'drabo diena'
    case 6 | 7:
        txt = 'savaitgalis'
    case _:
        print('blogai ivesti duomenys') #txt = 'blogai ivesti duomenys'
        viskasok = False

if viskasok :
    print(f'{diena} - {txt}')
