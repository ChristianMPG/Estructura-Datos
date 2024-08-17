x=float(input("Introduce tu peso en kg: "))
y=float(input("Introduce tu altura en m: "))

z=x/(y**2)

if z>25.0:
    print("Estas en sobrepeso")
elif z>18.5:
    print("Estas en un peso normal")
else:
    print("Estas en un peso bajo")



