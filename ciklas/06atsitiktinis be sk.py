# norime sugeneruoti stsitiktini skaiciu....
import random 
n = int(input('n=...'))
sk = random.randint(0, n) # sugeneruoja ir n
print(f'sk = {sk}')
sk1 = random.randrange(n) # sugeneruoja iki n
print(f'sk = {sk1}')
sk2 = random.randrange(1, n, 2) #nelyginiai skaiciai
print(f'sk = {sk2}')
sk3 = random.random() # nuo nulio iki vieneto
print(f'sk3 = {sk3}') # {int(sk3*100)} kad generuotu iki 100 !!!!!!