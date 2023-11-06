# mandagi programa, programa kuri visada sako labas
pasirinkimas = True
while pasirinkimas:
    print('labas')
    atsakymas = input('ar norite dar karta pasisveikinti (T/N)?')
    if atsakymas == 'T' or atsakymas == 't':
        continue
    else:
        pasirinkimas = False
        print('viso gero.....')