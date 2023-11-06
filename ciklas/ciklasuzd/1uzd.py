prad = int(input('iveskite pradine kaina...'))
moneta = 0
ivesta = 0
suma = 0
while suma<prad:
    moneta = int(input('imeskite moneta...'))
    if moneta == 1:
        moneta = 100
    elif moneta == 2:
        moneta = 200
    elif moneta==10:
        moneta = 10
    elif moneta==20:
        moneta = 20
    elif moneta==50:
        moneta = 50
    else:
        print('neteisinga moneta')
    suma += moneta 
    ivesta +=1
    if suma == prad:
        print(f'uz kava atsikaityta...{prad} sumokejote...{suma},bei metete {ivesta} monetu')
    elif suma>prad:
        print(f'uz kava atsikaityta...{prad} sumokejote...{suma}, graza{suma-prad},bei metete {ivesta} monetu')
    

