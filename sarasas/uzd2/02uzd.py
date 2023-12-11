
m = [1,5, 7, -4, 8, -3, 8]
nr = m.pop(0)
lyg = 0
nelyg = 0
s = 0
for i in range(len(m)):
    i+=1
    r = m.pop(0)
    if r > 0:
        lyg+=r
        s+=1
    else:
        r = r * -1
        nelyg+=r
vidL = lyg/s
vid = (lyg+nelyg)/i
print(f'Mokinys Nr. {nr} vidutkis HTML ir Python yra {round(vid,2)}. Tik HTML vidurkis {round(vidL,2)}')

    