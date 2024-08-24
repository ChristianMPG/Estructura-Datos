#crear un sistema de control de ingreso, para evitar el sobrecupo
#Condiciones: definir cual va a ser el número a controlar
#antes de permitir el ingreso debe solicitar el boleto de entrada
#si el boleto no es valido mostrar el mensaje "acceso no permitido", de lo contrario dejar entrar
# y contar el cupo
#cuando el cupo se llene completamente mostrar como mensaje final "no se permite más ingresos"

cupo =5
asientos=[]
print("Bienvenido")

while cupo >0:
    
    x =int(input(f"Digite su boleto de entrada de entrada, tenemos {cupo}"" acientos disponibles, ¿Cual desea?"))
    if x>=6:
        print("Número invalido")
    elif x<1:
        print("Número invalido")
    while 1<=x<=5:
        if x in asientos:
            print("Asiento ocupado, digíte un aciento disponible")
        else:
            if x==1:
                print(f"Bienvenido, tome su aciento #{x}")
                cupo -=1
                asientos.append(x)
            elif x==2:
                print(f"Bienvenido, tome su aciento #{x}")
                cupo -=1
                asientos.append(x)
            elif x==3:
                print(f"Bienvenido, tome su aciento #{x}")
                cupo -=1
                asientos.append(x)   
            elif x==4:
                print(f"Bienvenido, tome su aciento #{x}")
                cupo -=1
                asientos.append(x)   
            elif x==5:
                print(f"Bienvenido, tome su aciento #{x}")
                cupo -=1
                asientos.append(x)
            
        
            
        break        

print("Sala llena")



#control = 0
#cupo =int(input("Ingrese el cupo"))
#while control < cupo:
#    valido = input("¿voleto es valido? S/N")
#    if valido == "S" or valido == "s":
#        print("Persona ingresada")
#        control += 1
#    else:
#        print("persona no ingresa")    

#print ("Cupo lleno")   

       
        
        
        
                         










