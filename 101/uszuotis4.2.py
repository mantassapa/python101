p = int(input('iveskite prekiu kieki...'))
d = int(input('kiek telp i didele deze...'))
m = int(input('kiek telp i maza deze...'))

dkiek = p // d
dkiekis = d * dkiek
likutis = p % d 
mkiek = likutis // m
mkiekis = m * mkiek
liko = likutis % m

print(f'i {dkiek} dideles dezes {dkiekis} prekiu')
print(f'i {mkiek} mazas dezes {mkiekis} prekiu')
print(f'{liko} prekiu nepanaudotu')