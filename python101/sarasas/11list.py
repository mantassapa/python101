a = [5, 8, 7, 14, 9]
# reikia masyvo a kvadrato
b =[]
for i in a:
    el = i*i
    b.append(el)
print(b)

c=[i*i*i for i in a]
print(c)


#konvertacija i skaicius----------------------
txt = '52, 14, -15, 45, 14, 58, 47, 12'
# listtxt = txt.split(', ')
# print(listtxt)

sk = [int(i) for i in txt.split(', ')]
print(sk)
