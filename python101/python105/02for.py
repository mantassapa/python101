txt = 'man rytais labai patinka ąčęųsti keltis eiti į mokykla'
kiek = 0
lt = 'ąčęėįšųūžĄČĘĖĮŠŲŪŽ'
for i in txt:
    if i in lt:
        kiek += 1 # keik + kiek + 1
print(f'sakinyje "{txt}" yra {kiek} lietuvisku simboliu')