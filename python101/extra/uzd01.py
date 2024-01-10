viniesilgis = int(input('kokio ilgio viniv....'))
k = int(input('kiek cm vinies ikalama.....'))
for i in range(1, int((viniesilgis/k)+1)):
    viniesilgis = viniesilgis - k
    if viniesilgis > 0:
        print(f'Tuk! liko.. {i} -asis smugis. dar liko {viniesilgis}cm neikaltos vinies')
    else:
        print(f'Tuk! {i}-asis smugis vinis ikalta')
        break