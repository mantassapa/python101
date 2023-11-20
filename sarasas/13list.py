cmAukstis = [186,185,168,147,205,158,189,174,158]
colisAukstis = [round(cm / 2.45,2) for cm in cmAukstis]
print(colisAukstis)
# kitaip 

# coliai = []
# for i in cmAukstis:
#     el = round(2.45, 2)
#     coliai.append(el)
# print(coliai)

# sukurti elementu masyva kur zodelis aukst, jei ugis daugiau ne 186 ir vid ir maz jei mazesnis uz 156
ugisTxt = ['Aukst.' if i >= 186 else 'maz.' if i <= 156 else 'vid.' for i in cmAukstis] # reikia naudoti else ...else vietoj elif 
print(ugisTxt)