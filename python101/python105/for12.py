# apsakiaciuoti suma s = 1 +1/2 - 1/3 + 1/4 - 1/5 + 1/6-..+-1/n, n - musu skaicius
import math
n = int(input("n...."))
suma1 = suma = 1
for i in range(2, n):
    # if 1 % 2 == 0:
    #     suma = suma + 1/i
    # else:
    #     suma + suma - 1/i *(-1**i)
    if i == 1:
        i= 2
    else:
        i = 1
        suma = suma +(pow(-1, i)*(1/i))
print(suma)