# ivedame skaicius sk = 5
#  1 2 3 4 5 
#  1 2 3 4 5 
#  1 2 3 4 5 
#  1 2 3 4 5 
#  1 2 3 4 5 
sk = int(input('sk = '))
for j in range(0):
    for i in range(1,sk+1):
        if i != sk:
            print(i,end=(' '))
        else:
            print(i,)