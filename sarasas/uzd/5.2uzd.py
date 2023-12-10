a = [2, 4, 6, 8, 10, 12, 14]
b = [1, 3, 5, 7, 9, 11, 13]
c = []

for i in range(len(a)):
    d = a.pop(0)
    c.append(d)
    e = b.pop(0)
    c.append(e)
print(c)
