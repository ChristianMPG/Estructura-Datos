#Realizar la multiplicación de dos números por medio de sumas
def mult(a:int,b:int)->int:
    if a==0:
        return 0
    return b + mult(a-1,b) 
print(mult(4,5))    
        