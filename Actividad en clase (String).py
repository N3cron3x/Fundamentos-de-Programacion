dato = "oso, perro, 10, 5, son animales"

palabras = dato.split(',')

oso, perro, primer_num, segundo_num = palabras[0], palabras[1], palabras[2], palabras[3]
if oso == oso[::-1]:
    print(f"{oso} es un palíndromo")
else:
    print(f"{oso} no es un palíndromo")

if perro == perro[::-1]:
    print(f"{perro} es un palíndromo")
else:
    print(f"{perro} no es un palíndromo")

print(f"Tenemos{segundo_num} osos")

print(f"Tenemos{primer_num} perros")

print(f"Los {oso}s y los{perro}s son animales")