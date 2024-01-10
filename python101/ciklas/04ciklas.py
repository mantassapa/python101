# ivedame skaicius sk = 5
#  1 2 3 4 5
#  1 2 3 4
#  1 2 3
#  1 2
#  1 
sk = int(input('sk = '))
for j in range(1,sk+1):
    for i in range(1,sk-j+2):
        print(i,end=(' '))
    print()
# or
sk = int(input('sk = '))
for j in range(sk):
    for i in range(1,sk+1-j):
        print(i,end=(' '))
    print()
    