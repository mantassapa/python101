met = int(input('iveskite metus...'))

kiek = 0
i = 4

if met % i == 0:
    kiek += i
    print('Zmogus gime kelemaisiais metais')
else:
    print('Zmogus gime nekelemaisiais metais')
    