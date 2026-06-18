# Ejercicio: Valor dentro de un rango
valor = int(input("digite un numero: "))
valorMinimo = 0
valorMaximo = 7
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f"El valor {valor} esta dentro del rango")
else:
    print(f"El valor {valor} no esta dentro del rango")
