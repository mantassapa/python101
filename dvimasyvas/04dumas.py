
grupe = [['jonas', 5, 8,9,7,8],['tadas', 5,8,9,7,8],['antanas',9,8,9,9,10,8],['rimas',5,8,7,9,7,10,10],['vyc',4,4,3]]
gerStudNr = None
gerVid = 0

for stud in range(len(grupe)):
    sumPaz = 0
    for nrPaz in range(1,len(grupe[stud])):
        sumPaz += grupe[stud][nrPaz]
        #sum()
    vid = sumPaz / (len(grupe[stud])-1)
    grupe[stud].append(round(vid,2))
    if vid >= gerVid:
        gerVid = round(vid,2)
        gerStudNr = stud

print(f'Vardas {grupe[gerStudNr[0]]}')
print(f'viskas apie geriausia {grupe[gerStudNr]}')
print(f'viska grupe {grupe}')