#ivedamas pazimys jei nuo -... iki 0 negalimas balas 
#nuo 1 iki 3 blogas
#muo 4 iki 6 patenkinamas
#nuo 7 ik 9 geras
#10 puiku
#nuo 11 iki +... negalimas
p = int(input('iveskite pazimi...'))
if p >= 1 and p <= 3:
    print('blogas')
elif p >= 4 and p <= 6:
    print('patenkinamas')
elif p >= 7 and p <= 9:
    print('geras')
elif p == 10:
    print('puiku')
else:
    print("negalimas")
