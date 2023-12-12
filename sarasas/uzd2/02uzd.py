

def duomenys(masyvas):
    nr = masyvas.pop(0)
    lyg = 0
    nelyg = 0
    s = 0
    for i in range(len(masyvas)):
        i+=1
        r = masyvas.pop(0)
        if r > 0:
            lyg+=r
            s+=1
        else:
            r = r * -1
            nelyg+=r
    vidL = lyg/s
    vid = (lyg+nelyg)/i
    return print(f'Mokinys Nr. {nr} vidutkis HTML ir Python yra {round(vid,2)}. Tik HTML vidurkis {round(vidL,2)}')


duomenys([1, 5, 7, -4, 8, -3, 8]) 
duomenys([2, 4, 8, -2, 7, -2])
duomenys([3, 6, -4, 10, 9, -3, 8, -9])
duomenys([6, 5, 5, -2, 5, -9, 5, 4])
duomenys([17, 3, 5, 5, 4, -2, -5])
