prasek = int(input('iveskite sekundes...'))
minutes = prasek // 60
valandos = minutes // 60
sekundes = prasek % 100
print(f'{prasek}sek. = {valandos}val. {minutes}min. {sekundes}sek.')