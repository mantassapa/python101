#ivedamas skaicius perasyti ta sk atvirksciai....
# 12345 --> 54321
def atvirkstinis(skaicius):
    at = 0 
    while skaicius > 0:
        x1 = skaicius % 10
        skaicius = skaicius // 10
        at = at * 10 + x1
    return(suma)

sk = int(input('iveskite skaiciu...'))
s = atvirkstinis(sk)
print(f'skaicius{sk} parasius atvirksciai gausim {s}')