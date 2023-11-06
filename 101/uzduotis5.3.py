sk = int(input('iveskite seseziankli  sk...'))
sk1 = sk // 100000
sk2 = sk // 10000 % 10
sk3 = sk // 1000 % 10
sk4 = sk // 100 % 10
sk5 = sk // 10 % 10
sk6 = sk % 10
suma1 = sk2*sk5*sk6
suma2 = sk4+sk5+sk6
print(f'skaicius{sk} suma1{suma1} krastiniai{suma2}')
