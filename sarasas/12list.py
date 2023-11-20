#konvertacija is text i skaicius
# masyve butu tig lyginiai skaiciai
txt = '52, 14, -15, 45, 14, 58, 47, 12, 18, 12, 14'
sk = [int(i) for i in txt.split(', ')]
sklyg = [i for i in sk if i % 2 == 0]
print(sklyg)
# arba

# sk = [int(i) for i in txt.split(', ') if int(i) % 2 == 0]
# print(sk)

