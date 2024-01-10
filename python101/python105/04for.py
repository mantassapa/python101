#atspausdinti visus skaicius nuo 1 iki n, jei n daugiau uz 13 spausdinti iki 13
n = int(input('n='))
for i in range(1, n):
    print(i, end=', ' )
    if i == 13:
        break
else:
    print('\nviskas ok, ciklas nenutruko....')
print('\nprograma baige darba.....')