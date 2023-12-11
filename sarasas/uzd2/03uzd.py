
t = 16
n = [17, 16, 15, 17, 17, 19,18, 19, 17, 19, 17]#uzduotyje gautas 17 keturis kartus nors inrasytas penkis


n2 = []
te = 0
su = 0
max = 0
for i in n:
    if i not in n2:
        n2.append(i) 

for i in range(len(n2)):
    r = n.count(n2[i])
    print(f'{n2[i]} laipsniu temperatura buvo {r} d.')
    if max < r:
        max = r
for i in range(len(n)):
    if n[i] > t:
        su+=1

print(f'{su} dienas temperatura buvo didesne uz {t}')

print(f'Daugiausiai {max} dienas buvo')


    