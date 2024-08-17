x= int(input("Introduce un número: "))
y=int(input("Introduce otro número: "))
z=int(input("Introduce otro número: "))

if x>y:
    if x>z:
        print(f"{x} es el mayor")
        if y>z:
            print(f"{y} es el mayor")
        else:
            print(f"{z} es el mayor")
    else:
        print(f"{z} es el mayor")
        if x>y:
            print(f"{x} es el mayor")
        else:
            print(f"{y} es el mayor")
elif y>z:
    print(f"{y} es el mayor")
    if x>z:
            print(f"{x} es el mayor")
    else:
            print(f"{z} es el mayor")
else:
    print(f"{z} es el mayor")

    