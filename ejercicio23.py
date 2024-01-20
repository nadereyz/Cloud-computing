"""
1. Define dos listas de la compra iniciales, **`lista_compra_a`** y **`lista_compra_b`**, cada una con al menos cinco artículos (strings).
2. Crea conjuntos a partir de estas listas de la compra.
3. Implementa una función llamada **`agregar_articulos`** que acepte un conjunto de artículos y una lista de nuevos artículos,
y añada los nuevos artículos al conjunto. Asegúrate de que no se permitan artículos duplicados. Usa un bucle for.
4. Implementa una función llamada **`eliminar_articulos`** que acepte un conjunto de artículos y una lista de artículos existentes,
y elimine los artículos del conjunto. Usa un bucle for.
5. Utiliza las funciones para agregar y eliminar artículos de ambas listas de la compra.
6. Imprime las listas de la compra resultantes después de agregar y eliminar artículos.
"""

# 1
lista_compra_a = ["gyoza", "leche", "lentejas", "frutas", "empanadas"]
lista_compra_b = ["arroz", "pasta", "pescado", "queso", "galletas"]

print(lista_compra_a, "\n", lista_compra_b)
# 2
lista_a = set(lista_compra_a)
lista_b = set(lista_compra_b)
print("\n")

# 3
def agregar_articulos(conjunto_add, nuevos_articulos):
    for articulo in nuevos_articulos:
        conjunto_add.add(articulo)

# 4
def eliminar_articulos(conjunto_delete, articulos_existentes):
    for articulo in articulos_existentes:
        conjunto_delete.discard(articulo)

# 5
nuevos_articulos_a = ["cuscus", "poms", "harxa"]
eliminar_articulos_b = ["arroz", "queso", "pasta"]

agregar_articulos(lista_a, nuevos_articulos_a)
eliminar_articulos(lista_b, eliminar_articulos_b)

# 6
print("Lista de la compra A despues de agregar:", lista_a)
print("Lista de la compra B despues de eliminar:", lista_b)
