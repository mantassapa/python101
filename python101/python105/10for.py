# anukas turi x euru ir y centu. Senelis visa menesi (30 dienu) dave anukui po a centu. Parasyti programa kuri parodytu kiekvienos dienos anuko turimu pinigu kiek
#pavyzdziui anukas turi 20 euru. 30 ct. senelis duoda po 50 ct.
#rezultatas: 1 diena anukas tures 20 eur 80 centu

x = int(input('kiek anukas turi euru: '))
y = int(input('kiek anukas turi centu: '))
a = int(input('kiek senelis dave centu: '))
sumaCentais = x*100 + y
turi = a
for i in range(1, 31):
        x = 0
        turi += y
        print(f' {i} diena anukas tures {x} eur {turi} ct')