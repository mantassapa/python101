
t = 16
n = [17, 16, 15, 17, 17, 19,18, 19, 17, 19, 17]#uzduotyje gautas 17 keturis kartus nors inrasytas penkis
n.sort()

n2 = []
te = 0
su = 0
maxi = 0
for i in n:
    if i not in n2:
        n2.append(i) 

for i in range(len(n2)):
    r = n.count(n2[i])
    print(f'{n2[i]} laipsniu temperatura buvo {r} d.')
    if maxi < r:
        maxi = r
for i in range(len(n)):
    if n[i] > t:
        su+=1

print(f'{su} dienas temperatura buvo didesne uz {t}')


def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
 
print(f'Daugiausiai {maxi} dienas buvo {most_frequent(n)}')


    