

while True:
    try:
        sk = int(input('iveskite skaiciu = '))
        break
    except ValueError as ex:
        print(f'Klaidos pranesimas {ex}. Kartokite ivedima')


print(f'sk = {sk}')