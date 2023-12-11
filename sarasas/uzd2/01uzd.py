
m = [7,7,15,15,18,20,21]
m2 = []


for i in range(len(m)):
    r = m.pop(0)
    if m:
        r2 = m.pop(0)
        if r == r2:
            suma = r+r2
            m.insert(0,suma)
            print(f'{i+1} kova. lygiosios. skaiciai susijungia')
            print(m)
        elif r < r2:
            suma = r2 - r + r2
            m.insert(0,suma)
            print(f'{i+1} kova antras skaicius sunaikina pirma')
            print(m)
        elif r > r2:
            suma = r - r2 + r
            m.insert(0,suma)
            print(f'{i+1} kova pirmas skaicius sunaikina pirma')
            print(m)
    else:
        break
