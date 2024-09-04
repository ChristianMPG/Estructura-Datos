#verificar si una palabra dada es un palindromo
def reversa(palabra:str)->str:
    txt = f"{palabra}"[::-1]
    if palabra == txt:
        return f"La palabra {palabra}  se lee igual a {txt}  al revés, por ende es un palindromo"
    else:
        return f"La palabra {palabra} no se lee igual a {txt} al revés, por ende esun palindromo"
    
palabra=str(input("Digite la palabra que desea saber si es un palindromo"))
print(reversa(palabra))