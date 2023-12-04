# r - nuskaito visa faila
# a - papildyti
# w - perasyti (sukuria faila is naujo)
# r+ - ir skaityti ir rasyti

with open('02data.txt', 'r+', encoding='utf=8') as f:
    txt = f.read()
    print(txt)
    f.seek(0) #sugrazina zymekli i pradzia
    # t1 = f.readline()
    # print(type(t1))
    t1 = int(f.readline())
    t2 = int(f.readline())
    t3 = int(f.readline())
    s = t1 + t2 + t3
    f.write(f'\n{t1} + {t2} + {t3} = {s}\n')