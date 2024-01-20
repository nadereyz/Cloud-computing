"""
1. Define dos listas de reproducción iniciales, **`playlist_a`** y **`playlist_b`**, cada una con al menos cinco canciones representadas por nombres de canciones (strings).
2. Crea conjuntos a partir de estas listas de reproducción.
3. Implementa una función llamada **`agregar_cancion`** que acepte un conjunto de canciones y el nombre de una nueva canción, y añada la nueva canción al conjunto. Asegúrate de que no se permitan canciones duplicadas.
4. Implementa una función llamada **`eliminar_cancion`** que acepte un conjunto de canciones y el nombre de una canción existente, y elimine la canción del conjunto.
5. Utiliza el método de conjunto **`union`** para crear una nueva lista de reproducción que contenga todas las canciones de **`playlist_a`** y **`playlist_b`**.
6. Utiliza el método de conjunto **`intersection`** para crear una nueva lista de reproducción que contenga solo las canciones que están en ambas **`playlist_a`** y **`playlist_b`**.
7. Utiliza el método de conjunto **`difference`** para crear una nueva lista de reproducción que contenga las canciones que están en **`playlist_a`** pero no en **`playlist_b`**.
8. Imprime las listas de reproducción resultantes y verifica que las funciones y métodos están trabajando correctamente.
"""
# 1
playlist_a = {"llamada de emergencia", "san holo fly", "Diosa del Perreo", "Aurora Sintética", "Galaxia Vibrante"}
playlist_b = {"Amanecer sin Ti", "Ritmo Prohibido", "Entre Sombras", "Neón Nocturno", "Viaje Cibernético"}
""
# 2

set_a = set(playlist_a)
set_b = set(playlist_b)

# 3
def agregar_cancion(conjunto, nueva_cancion):
    conjunto.add(nueva_cancion)

agregar_cancion(set_a, "Cancion9")
print(set_a | set_b)

# 4
def eliminar_cancion(conjunto, eliminar_cancion):
    conjunto.discard(eliminar_cancion)
eliminar_cancion(playlist_a, "Ritmo Prohibido")
print(set_a | set_b)



# 5
union_listas = playlist_a.union(playlist_b)

# 6
interseccion_listas = playlist_a.intersection(playlist_b)

# 7
diferencia_listas = playlist_a.difference(playlist_b)

# 8
print("Playlist A:", playlist_a)
print("Playlist B:", playlist_b)
print("Union:", union_listas)
print("intersection:", interseccion_listas)
print("difference:", diferencia_listas)
