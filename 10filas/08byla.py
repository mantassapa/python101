def skaitytiDuom():
    with open('08data.txt', 'r', encoding='utf-8') as f :
        txt = []
        while True:
            eil = f.readline()
            if eil:
                txt.append(eil)
            else:
                break
    return txt

visiData = skaitytiDuom()
skaiciai = []
for eil in visiData:
    eilSk = [int(x) for x in eil.split() if x != '\n']
    skaiciai.append(eilSk)
# print(skaiciai)
print(skaiciai[0][0])