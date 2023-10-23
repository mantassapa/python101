prad = int(input('iveskite pradine kaina...'))
moneta = int(input('imeskite moneta...'))
suma = 0
if suma<=prad: 
    suma += moneta
    moneta = int(input('imeskite dar moneta'))
    print('uz kava atsikaityta')
else:
    return moneta