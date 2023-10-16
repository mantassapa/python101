savDiena = int(input('kokia savaites diena prasideda menuo?  '))
a = int(input('saraso pradzia....'))
b = int(input('saraso pabaiga....'))
for i in range(1, 32):
    if a<=i<=b:
        print(f'{i}-oji menesio diena bus {savDiena}')         
    if savDiena == 7:
        savDiena = 1   
    else:
        savDiena =+1
    if i==b:
        break

