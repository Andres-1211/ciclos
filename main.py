#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
#El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

def calcular_tiempo_total():
    total_minutos = 0
    
    while True:
        
        duracion_tramo = int(input("Duracion tramo: "))
        
      
        if duracion_tramo == 0:
            break
        

        
      
        total_minutos += duracion_tramo
    
  
    horas = total_minutos // 60
    minutos = total_minutos % 60
    
   
    print(f"Tiempo total de viaje: {horas}:{minutos:} horas")
calcular_tiempo_total()

