#def calcular_Promedio(n1:int,n2:int, nombre:str)-> int: #la flecha indica que devuelve un tipo de dato
#    return

#Crear una función que calcule el factorial de un número, como parametro de entrada
#debe recibir el número a calcular

def calculo_Facotrial(numero:int)->str|int:
    resultado = 1
    if numero<0:
        return"Valor invalido, digite un número positivo"
    for n in range(1,numero+1):
        resultado = resultado*n
    return resultado    

#op1:

facotrial = calculo_Facotrial(-5)
print("El resultado del factorial es: ",facotrial)

#op2:
print("El facotorial es: ",calculo_Facotrial(0) ) 