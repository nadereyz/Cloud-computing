# crear lista

mi_lista = [1, 2, 3, 0.5, "string", "mi segundo string", True]

#acceder a cualquier elemento de la lista

print(mi_lista[1])
elemento_cuarto = mi_lista[3]
#modificar los elementos de una lista

mi_lista[3] = 100
print(mi_lista)

#metodo len (calcular la longitud o numeros de los elementos en una lista)
print(len(mi_lista)) 

#append (es para añadir los elementos al final de una lista)

mi_lista.append("soy el ultimo")

print(mi_lista)


#eliminar elementos de mi lista -> remove
# hay dos forma de eliminar uno por el valor o determinar cual es el indice.

# mi_lista.remove(2) -> hay un numero 2 y quiero borrar, con esto se borra directamente el valor

mi_lista.remove(2)

# mi.lista.remove(mi_lista[4]) eso lo que borrara es String
mi_lista.remove(mi_lista[3])
print(mi_lista)


#buscar el indice de un elemento 
print(mi_lista.index("soy el ultimo"))


# eliminar todo el elemento de la lista -> clear

mi_lista.clear()
print(mi_lista)

#programa para agregar nombres a una lista

lista_canciones = []

cancion1 = str(input("añade tu 1 cancion fav:  "))
lista_canciones.append(cancion1)
cancion2 = str(input("añade tu 2 cancion fav: "))
lista_canciones.append(cancion2)
cancion3 = str(input("añade tu 3 cancion fav: "))
lista_canciones.append(cancion3)
cancion3 = str(input("añade tu 4 cancion fav: "))
lista_canciones.append(cancion3)
cancion3 = str(input("añade tu 5 cancion fav: "))
lista_canciones.append(cancion3)

print(lista_canciones)

