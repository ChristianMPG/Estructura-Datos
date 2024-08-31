#Crear una función que convierta temperatura Celcius a Fahrenheit
def convertir(n1:float)->float:
    fa=((n1*9)/5)+32
    return fa
n1=float(input("Digite los grados celcius a convertir a Farenheit"))
print(f"Los grados farenheit son {convertir(n1)}")