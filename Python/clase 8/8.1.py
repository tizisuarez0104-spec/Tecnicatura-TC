while True:
    print("Comprobamos que año es bisiesto")
    num = int(input("Ingrese el año: "))

    if ((num % 4 == 0) and (num % 100 != 0)) or (num % 400 == 0):
        print("El año es Bisiesto")
    else:
        print("El año no es Bisiesto")

    opcion = int(input("Para seguir adelante digite la opcion 1: "))

    if opcion != 1:
        break