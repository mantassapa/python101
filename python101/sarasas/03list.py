m = [5, 6, 8, 7, 14, 15, -85,-8, 13, 17]
a = m.copy()
print(id(m))
print(id(a))
dalislist = m[1:6:2]
print(dalislist)
b = m[0:-1] #neimas paskutinio
print(b)
c = m[0:len(m)]
print(b)
print(c)
d = m[::] #kitas c variantas
print(d)