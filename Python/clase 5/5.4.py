# Ejercicio: Rango entre 20 y 30 años

edad = int(input("Digite su edad: "))

veinte = edad >= 20 and edad < 30
print(veinte)

treinta = edad >= 30 and edad < 40
print(treinta)

if veinte:
    print("Estás dentro del rango de los 20⁄0 años.")
elif treinta:
    print("Estás dentro del rango de los 30/0 años.")
else:
    print("No estás dentro del rango de los 20 a los 39 años.")