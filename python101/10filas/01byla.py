# r - nuskaito visa faila
# a - papildyti
# w - perasyti
# f.write(f'\n{x} + {y} = {x+y}\n')
# f.close()


# f = open('01data1.txt', 'w', encoding='utf=8')
# f.write('pirmas kartas su failu \n')
# f.write('ąčęėįšųū')
# a = [8, 8,5,6,9]
# f.write(a)   <-- kad klaida mestu
# f.write(str(a))
# x = 5
# y = 8
# f.write(f'\n{x} + {y} = {x+y}\n')
# f.close()

# try:
#     f = open('01data1.txt', 'w', encoding='utf=8')
#     f.write('pirmas kartas su failu \n')
#     f.write('ąčęėįšųū')
#     a = [8, 8,5,6,9]
#     f.write(a)
#     f.write(str(a))
#     x = 5
#     y = 8
#     f.write(f'\n{x} + {y} = {x+y}\n')
# finally:
#     f.close()

# with open('01data1.txt', 'w', encoding='utf=8') as f:
#     f.write('pirmas kartas su failu \n')
#     f.write('ąčęėįšųū')
#     a = [8, 8,5,6,9]
#     f.write(a)
#     f.write(str(a))
#     x = 5
#     y = 8
#     f.write(f'\n{x} + {y} = {x+y}\n')
