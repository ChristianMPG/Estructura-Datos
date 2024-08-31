#Crear una función que realice operaciones basicas(suma, resta, divison, multiplicacion)enre dos numeros
def op_Basicas(n1:int,n2:int,op:int)->int:
    if op== 1:
        sum=n1+n2
        return f"La suma entre {n1} y {n2} es {sum}"
    elif op==2:      
        res=n1-n1
        return f"La resta entre {n1} y {n2} es {res}"
    elif op==3:
        mult=n1*n2
        return f"La multiplicación entre {n1} y {n2} es {mult}"
    elif op==4:
        div=float(n1/n2)
        return f"La división entre {n1} y {n2} es {div}"

    
    




print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")
op=int(input("Digite la opción que desea realizar:"))

if op ==1 or op==2 or op==3 or op==4:
    n1=int(input("Digite el primer número"))
    n2=int(input("Digite el segundo número"))
    print( op_Basicas(n1,n2,op))
    
        
    




                  


     
    
    
    
