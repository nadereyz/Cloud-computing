"""
1. Define un diccionario llamado **`biblioteca`** con al menos cinco libros y la cantidad de ejemplares disponibles para cada uno.
2. Implementa una función llamada **`prestar_libro`** que acepte el título de un libro y la cantidad de ejemplares que se van a prestar. 
    La función deberá restar la cantidad prestada del total de ejemplares disponibles. Asegúrate de manejar casos en los que la cantidad prestada sea mayor que la cantidad disponible.
3. Implementa una función llamada **`devolver_libro`** que acepte el título de un libro y la cantidad de ejemplares que se van a devolver. 
    La función deberá sumar la cantidad devuelta al total de ejemplares disponibles. Asegúrate de manejar casos en los que la cantidad devuelta sea mayor que la cantidad prestada.
4. Implementa una función llamada **`ver_inventario`** que imprima todos los libros en la biblioteca y la cantidad de ejemplares disponibles.
5. Utiliza las funciones para realizar operaciones de préstamo, devolución e imprimir el inventario.
"""

biblioteca = {
    "Renacer": 10,
    "Justicia": 8,
    "Aventura": 5,
    "Destino": 12,
    "Silencio": 15
}

# 2
def prestar_libro(titulo, cantidad):
    if titulo in biblioteca and biblioteca[titulo] >= cantidad:
        biblioteca[titulo] -= cantidad
        print(f"Se prestaron {cantidad} ejemplares del libro '{titulo}'.")
    else:
        print(f"No hay suficientes ejemplares disponibles para el libro '{titulo}'.")

# 3
def devolver_libro(titulo, cantidad):
    if titulo in biblioteca:
        biblioteca[titulo] += cantidad
        print(f"Se devolvieron {cantidad} ejemplares del libro '{titulo}'.")
    else:
        print(f"El libro '{titulo}' no está en la biblioteca.")

# 4
def ver_inventario():
    print("Inventario de la biblioteca:")
    for libro, cantidad in biblioteca.items():
        print(f"{libro}: {cantidad} ejemplares disponibles")


# 5

ver_inventario()

prestar_libro("Renacer", 3)
prestar_libro("Justicia", 10)
prestar_libro("Aventura", 2)

ver_inventario()

devolver_libro("Destino", 5)
devolver_libro("Silencio", 8)

ver_inventario()


