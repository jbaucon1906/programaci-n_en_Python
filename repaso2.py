numero = float(input("introduce un numero"))

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print ("El numero es negativo")
else:
    print ("El numero es cero")


año = int(input("Ingresa un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
