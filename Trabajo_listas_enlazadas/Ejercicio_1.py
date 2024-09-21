# Diseñe e implemente un sistema para el control de un sistema de un parque Zoologico 
#Crear una clase animal con los métodos y atributos básicos. en uno de los atributos,
#  debes indicar la edad y el tipo de animal (Águila, pantera, vaca, ...)
#Crear una lista enlazada que permita agregar animales al listado, 
# donde al momento de agregar un nuevo animal a la lista, esta no debe repetirse
#Para mostrar los animales que contiene la lista enlazada, debes realizarla usando dos métodos
#Una función recursiva y Un bucle

class Animal:
    def __init__(self, edad: int, tipo: str) -> None:
        self.tipo = tipo
        self.edad = edad

    def __eq__(self, other):
        return self.tipo == other.tipo and self.edad == other.edad

    def __str__(self):
        return f"Animal: {self.tipo}, Edad: {self.edad}"


class Node:
    def __init__(self, animal: Animal):
        self.animal = animal
        self.next = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def es_vacio(self):
        return self.cabeza is None

    def agregar_nodo(self, animal: Animal):
        if self.buscar_elemento(animal):
            print(f"El animal {animal.tipo} ya está en la lista.")
            return

        nodo = Node(animal)
        if self.es_vacio():
            self.cabeza = nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next is not None:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nodo

    def imprimir(self):
        nodo_actual = self.cabeza
        if self.es_vacio():
            print("La lista está vacía.")
            return
        while nodo_actual is not None:
            print(nodo_actual.animal)
            nodo_actual = nodo_actual.next

    def imprimir_recursivo(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
        if nodo is not None:
            print(nodo.animal)
            self.imprimir_recursivo(nodo.next)

    def eliminar(self, animal: Animal):
        nodo_actual = self.cabeza
        anterior = None
        while nodo_actual is not None:
            if nodo_actual.animal == animal:
                if anterior is None:  
                    self.cabeza = nodo_actual.next
                else:
                    anterior.next = nodo_actual.next
                print(f"El animal {animal.tipo} ha sido eliminado.")
                return
            anterior = nodo_actual
            nodo_actual = nodo_actual.next
        print(f"El animal {animal.tipo} no fue encontrado en la lista.")

    def buscar_elemento(self, animal: Animal):
        nodo_actual = self.cabeza
        c = 0
        while nodo_actual is not None:
            if nodo_actual.animal == animal:
                return f"El animal {nodo_actual.animal} está en la posición {c}"
            nodo_actual = nodo_actual.next
            c += 1
        return None  



def mostrar_menu():
    print("\n--- Sistema de Control del Parque Zoológico ---")
    print("1. Agregar un animal")
    print("2. Eliminar un animal")
    print("3. Mostrar animales (bucle)")
    print("4. Mostrar animales (recursivo)")
    print("5. Buscar un animal")
    print("6. Salir")
    print("----------------------------------------------")



def main():
    zoologico = ListaEnlazada()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Ingrese el tipo de animal: ")
            edad = int(input("Ingrese la edad del animal: "))
            nuevo_animal = Animal(edad, tipo)
            zoologico.agregar_nodo(nuevo_animal)

        elif opcion == "2":
            tipo = input("Ingrese el tipo de animal a eliminar: ")
            edad = int(input("Ingrese la edad del animal a eliminar: "))
            zoologico.eliminar(Animal(edad, tipo))

        elif opcion == "3":
            print("\nLista de animales (bucle):")
            zoologico.imprimir()

        elif opcion == "4":
            print("\nLista de animales (recursivo):")
            zoologico.imprimir_recursivo()

        elif opcion == "5":
            tipo = input("Ingrese el tipo de animal a buscar: ")
            edad = int(input("Ingrese la edad del animal a buscar: "))
            resultado = zoologico.buscar_elemento(Animal(edad, tipo))
            if resultado:
                print(resultado)
            else:
                print(f"El animal {tipo} no se encuentra en la lista.")

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Por favor seleccione una opción válida.")



if __name__ == "__main__":
    main()