m = int(input('iveskite sesezianki skaiciu m...'))
n = int(input('iveskite sesezianki skaiciu n...'))
kiek = 0
for i in range(m, n+1):
    sk1 = i//1000
    sk2 = i//100%10
    sk3 = i//10%10
    sk4 = i%10
    suma = sk2*100+sk3*10+sk4
    if sk1 == suma :
        kiek +=1
print(f'laimingus bilietus isigijo {kiek} keleiviu')