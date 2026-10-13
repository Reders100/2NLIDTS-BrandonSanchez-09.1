
class Nodo:
    def __init__(self):
        self.dato = 0
        self.siguiente = None


# Función Agregar elementos a la lista
def agregarNodo(cabeza, valor):
    nuevoNodo = Nodo()  # Creando la referencia hacia el nuevo nodo
    nuevoNodo.dato = valor
    nuevoNodo.siguiente = None

    if cabeza is None:
        cabeza = nuevoNodo
    else:
        actual = cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevoNodo

    return cabeza


def imprimirlista(cabeza):
    actual = cabeza
    while actual is not None:
        print(actual.dato, end=" ")
        actual = actual.siguiente
    print()


def borrarLista(cabeza):
    while cabeza is not None:
        siguiente = cabeza.siguiente
        # delete cabeza -> en Python se simula mostrando la "dirección" (id) del nodo liberado
        print("Elemento borrado", id(cabeza), end=" ")
        print("")
        cabeza = siguiente


def main():
    cabeza = None  # Declaramos una referencia nula
    tamanoLista = int(input("Ingrese la cantidad de elementos que desea agregar a la lista:"))

    if tamanoLista <= 0:
        print("Cantidad de elementos no valida")
        return 1

    for i in range(tamanoLista):
        valor = int(input("Ingrese dato " + str(i + 1) + ": "))
        ### Invocamos nuestra funcion de agregar Nodo
        cabeza = agregarNodo(cabeza, valor)

    print("Imprimiendo Lista de numeros")
    imprimirlista(cabeza)

    borrarLista(cabeza)

    return 0


main()