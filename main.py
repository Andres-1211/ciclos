#Escriba un programa que muestre una tabla de multiplicar como la siguiente:


size = 10


for columna in range(1, size +1):
   
    for fila in range(1, size +1):
        print(f"{columna * fila:4}", end="")
    print()