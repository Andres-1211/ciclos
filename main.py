#Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:

numero = int(input("ingrese un numero para la tabla: "))
i = 1
while True:
    
    print(f"{numero} * {i} = {numero * i}")
    i += 1
    if i > 10:
     break
    