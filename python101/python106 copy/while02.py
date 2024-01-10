# petriukas ...
kiek = int(input('kiek petriukas turi pazimiu'))
kelintas = 0
suma=0
while kiek > kelintas:
    kelintas +=1
    paz = int(input(f'iveskite petriuko {kelintas}-aji pazymi'))
    if 1<=paz<=10:
        suma+=paz
    else:
        print('blogas pazimys. kartokite ivedima')
        kelintas-=1
vid = suma / kiek
print(vid)