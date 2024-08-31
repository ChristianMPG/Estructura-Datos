#Crear una funcion que genere contraseñas aleatorias. La cantidad de caracteres a generar se envia por parametro
import random
import string

def generar_contrasena():
    longitud = int(input("Introduce la longitud de la contraseña: "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

print(generar_contrasena())

