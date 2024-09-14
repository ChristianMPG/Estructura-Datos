class Numero:
    def __init__(self,valor:int):
        self.valor = valor
    
    def __eq__(self,compara):
        return self.valor == compara

#Dirección de memoria:
# print(dir(a))   