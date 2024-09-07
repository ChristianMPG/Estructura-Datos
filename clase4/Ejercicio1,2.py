#1.Crear una clase llamada Vehículo, esta clase debe recibir 2 parámetros, marca y combustible; 
#la clase también debe contener dos métodos encender y arrancar. 
#Instanciar la clase y usar el método mágico __str__ para imprimir la marca y el combustible usado

#2.Crear dos clases, Moto y Carro, estas clases deben estar heradadas de la clase Vehiculo. 
#Realizar dos instancias de las nuevas clases creadas e imprimir el objeto instanciado

#1
class Vehiculo:
    def __init__(self,marca:str,combustible:str):
        self.marca=marca
        self.combustible=combustible
    
    def encender(self):
        pass
    def arrancar(self):
        pass
    def __str__(self) -> str:
        return f"la marca del vehiculo es {self.marca} y el combustible es {self.combustible}"
    
carro=Vehiculo("toyota","corriente")
print(carro)
#print(type(carro))

#2
class Moto(Vehiculo):
    def __init__(self, marca:str, combustible:str):  #se hace por si quiero añadir otro parámetro 
        super().__init__(marca,combustible)          #aparte de los heredados
    
    def __str__(self) -> str:
        return f"La moto es de marca {self.marca} y su combustible es {self.combustible}"
class Carro(Vehiculo):
    def __str__(self) -> str:
        return f"el carro es de marca {self.marca} y su combustible es {self.combustible}"


carro2=Carro("mazda","extra")
print(carro2)
moto=Moto("suzuki","corriente")
print(moto)
