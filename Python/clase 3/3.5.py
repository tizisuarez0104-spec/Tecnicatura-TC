miVariable = 3
print(miVariable)
miVariable = "hola a todos "
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))

#Las literales se escriben x240, la variable y = x984, la variable z = x304
print(id(y))
print(id(z))

##Tipos int, float, Sting, Bool
x = 10
print(x)
print(type(x))
x  = 14.5
print(x)
print(type(x))
x = "hola a todos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas (String)
miGrupoFavorito = "Tv De Los 90:"
caracteristicas = "Banda local"
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)

numero1 = ("8")
numero2 = ("9")
print(int(numero1) + int(numero2))

##Tipos Booleano (bool)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")
