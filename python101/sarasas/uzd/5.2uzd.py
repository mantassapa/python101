a = [2, 4, 6, 8, 10, 12, 14]
b = [1, 3, 5, 7, 9, 11, 13]
c = []
a.reverse()
b.reverse()
padetis = 0
for i in range(len(a)):
    A = a.pop(i)
    c.append(A)
    B = b.pop(i)
    c.append(B)
print(c)



print(c)
