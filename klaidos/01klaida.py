# try:
#     sk = int(input('iveskite skaiciu = '))
# except ValueError:
#     print('Blogai ivesti dupmenys, mums reikia sveiko skaiciaus')
#     sk = int(input('iveskite skaiciu = '))

while True:
    try:
        sk = int(input('iveskite skaiciu = '))
        break
    except ValueError:
        print('Blogai ivesti dupmenys, mums reikia sveiko skaiciaus')


print(f'sk = {sk}')