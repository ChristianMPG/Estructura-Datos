#Hacer control de encendido de los vehiculos, para esto al momento de usar el método encender, 
# se debe validar el nivel de combustible del vehiculo (medida dada en galones) no este por debajo 
# de un 10%, si este tiene un nivel muy bajo, mostrar la advertencia que necesita ir a la gasolinera. 
import random
class Vehiculo:
    def __init__(self,marca:str,combustible:str, galones:int):
        self.marca=marca
        self.combustible=combustible
        self.galones=galones
    
    def encender(self):
        # Generar un número aleatorio con decimales entre 0 y 10
        numero_aleatorio = random.uniform(0, 10)
        if numero_aleatorio < (self.galones*0.1):
            print (f"Necesita ir a la gasolinería, usted tine {numero_aleatorio}galones")
        else:
            print(f"Usted tiene {numero_aleatorio} litros, ¡gasolina optima!")

    def arrancar(self):
        pass
    
    
carro=Vehiculo("toyota","corriente",10)

carro.encender()
