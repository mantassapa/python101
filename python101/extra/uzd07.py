n = int(input('iveskite kiek bus eiliu n=...'))
k = int(input('iveskte kiek pirmoje eileje bus kedziuk=...'))
sk = 0
for i in range(1,n+1):
    sk +=2
    s = n * k + sk
print(f'reikia uzsakyti s = {s} kedziu')