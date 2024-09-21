from datetime import datetime

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def es_vacio(self):
        return self.cabeza is None

    def agregar_nodo(self, dato):
        nodo = Node(dato)
        if self.es_vacio():
            self.cabeza = nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next is not None:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nodo

    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.data)
            nodo_actual = nodo_actual.next

    def eliminar(self, dato):
        nodo_actual = self.cabeza
        if nodo_actual and nodo_actual.data.descripcion == dato:
            self.cabeza = nodo_actual.next
            return
        while nodo_actual and nodo_actual.next:
            if nodo_actual.next.data.descripcion == dato:
                nodo_actual.next = nodo_actual.next.next
                return
            nodo_actual = nodo_actual.next

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento

    def __str__(self):
        return f"Descripción: {self.descripcion}, Prioridad: {self.prioridad}, Fecha de vencimiento: {self.fecha_vencimiento.strftime('%Y-%m-%d')}"

class SistemaGestionTareas:
    def __init__(self):
        self.lista_tareas = ListaEnlazada()

    def agregar_tarea(self):
        descripcion = input("Ingrese la descripción de la tarea: ")
        prioridad = int(input("Ingrese la prioridad de la tarea (1-3): "))
        fecha_str = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
        fecha_vencimiento = datetime.strptime(fecha_str, "%Y-%m-%d")
        tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
        self.lista_tareas.agregar_nodo(tarea)
        print("Tarea agregada con éxito.")

    def eliminar_tarea(self):
        descripcion = input("Ingrese la descripción de la tarea a eliminar: ")
        self.lista_tareas.eliminar(descripcion)
        print("Tarea eliminada con éxito.")

    def mostrar_tareas(self):
        if self.lista_tareas.es_vacio():
            print("No hay tareas registradas.")
        else:
            self.lista_tareas.imprimir()

    def buscar_tarea(self):
        descripcion = input("Ingrese la descripción de la tarea a buscar: ")
        nodo_actual = self.lista_tareas.cabeza
        while nodo_actual:
            if nodo_actual.data.descripcion == descripcion:
                print("Tarea encontrada:")
                print(nodo_actual.data)
                return
            nodo_actual = nodo_actual.next
        print("Tarea no encontrada.")

    def marcar_completada(self):
        descripcion = input("Ingrese la descripción de la tarea completada: ")
        self.lista_tareas.eliminar(descripcion)
        print("Tarea marcada como completada y eliminada de la lista.")

def menu():
    sistema = SistemaGestionTareas()
    while True:
        print("\n--- Sistema de Gestión de Tareas ---")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar todas las tareas")
        print("4. Buscar tarea")
        print("5. Marcar tarea como completada")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.agregar_tarea()
        elif opcion == "2":
            sistema.eliminar_tarea()
        elif opcion == "3":
            sistema.mostrar_tareas()
        elif opcion == "4":
            sistema.buscar_tarea()
        elif opcion == "5":
            sistema.marcar_completada()
        elif opcion == "6":
            print("Gracias por usar el Sistema de Gestión de Tareas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()