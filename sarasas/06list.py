m = [5, 6, 1, 2, 8, 7, 14, 15, 2, 2, -85,-8, 13, 17]
did = max(m)
print(did)
maz = min(m)
print(maz)
mazel = m[0]
for i in m:
    if mazel > i:
        mazel = i
# for i in range(1,len(m)): #nelygina pacio saves
    # if mazel>m[i]:
    #     mazel = m[i]
print(mazel)

suma = sum(m)
print(suma)

m.sort()
print(m)
m.reverse() # nerikiuoja, tik paraso is kitos puses
print(m)

m.sort(reverse=True) #surusiuoja bei apsuka
print(m)

el = m.pop()
print(el)
print(m)

el2 = m.pop(2)
print(el2)
print(m)

m.remove(2)
print(m)
# arba
m.remove(m[4])
print(m)

print(m.count(2))
print(m.index(2))