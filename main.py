#Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:

altura = int(input("ingrese la altura "))
ancho = int(input("ingrese el ancho "))

print(f"altura:{altura}")
print(f"ancho:{ancho}")
for altura in range(1, altura +1):
    for ancho in range(1, ancho +1):
          
          print(f"*", end = " ")
    print()
#Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:

altura = int(input("Ingresa la altura del triángulo: "))


for altura in range(1, altura + 1):
    print('*' * altura)

