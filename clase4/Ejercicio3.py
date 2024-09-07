#La clase Vehiculo, debe tener una propiedad llamada tipo (esta contendrá el tipo de vehiculo - Carro 
# o Moto -), esta propiedad debe ser seteada al momento de instanciar la clase Carro o Moto y 
# al momento de imprimir el objeto debe indicar el tipo de vehiculo junto con el texto mostrado 
# anteriormente 

class Vehiculo:
    def __init__(self,marca:str,combustible:str,tipo:str):
        self.marca=marca
        self.combustible=combustible
        self.tipo=tipo
    
    def encender(self):
        pass
    def arrancar(self):
        pass
    def __str__(self) -> str:
        return f"la marca del vehiculo es {self.marca}  , el combustible es {self.combustible} y es un {self.tipo}"
    
carro=Vehiculo("toyota","corriente","carro")
print(carro)

