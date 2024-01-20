#Listas de reproducción
playlist_a = ["canción1", "canción2", "canción3", "canción4", "canción5"]
playlist_b = ["canción6,", "canción5", "canción7", "canción2", "canción8"]

#Conjunto de estas listas
set_a = set(playlist_a)
set_b = set(playlist_b)

#Agregar canción
def agregar_cancion(conjunto, nueva_cancion):    
    conjunto.add(nueva_cancion)

agregar_cancion(set_a, "canción2")
print(set_a | set_b)

#Eliminar canción del conjunto
def eliminar_cancion(conjunto, nueva_cancion_dos):    
    conjunto.remove(nueva_cancion_dos)

eliminar_cancion(set_a, "cancion924")
print(set_a | set_b)

# 5. Unir dos conjuntos
playlist_union = set_a.union(set_b)

# 6. Intersección de dos conjuntos
playlist_interseccion = set_a.intersection(set_b)

# 7. Diferencia de dos conjuntos
playlist_diferencia = set_a.difference(set_b)

# 8. Imprimir resultados
print("Playlist A:", set_a)
print("Playlist B:", set_b)
print("Unión de Playlists A y B:", playlist_union)
print("Intersección de Playlists A y B:", playlist_interseccion)
print("Diferencia de Playlists A y B:", playlist_diferencia)