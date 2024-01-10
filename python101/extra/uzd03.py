n = int(input('n....'))
sk = 0
suma = 0
for i in range (n):
    if i < n - 1:
        txt = ' + '
    else:
        txt = ' = '
    sk = sk * 10 + 7 
    print(sk, end=(txt))
    suma += sk
print(f' = {suma}')
