#atspausdinti visus skaicius nuo 1 iki n, jei n lygu 13, jo nespausdinti
n = int(input('n='))
for i in range(1, n):
    print(1, end=', ' )
    if i == 13:
        continue
    print(i, end=', ' )
else:
    print('\nviskas ok, ciklas nenutruko....')
print('\nprograma baige darba.....')