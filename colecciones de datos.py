# Listas
# Tuplas
# Conjuntos
# Diccionarios


# Listas:

lista1 = ["Hola", "Adios"]

print(lista1[0])

lista1[0] = "OtraVezHola"

print(lista1[0])

#- len: comprueba la longitud o número de elementos de una lista 


print(len(lista1))

# append: permite añadir un elemento al final de una lista

lista1.append("NosVemos")

print(lista1)

# remove: permite borrar elementos de una lista con el elemento o el índice

# hay 2 formas de utilizar remove.
#---------------------------
#lista1.remove("Adios")
#lista1.remove(lista1[0])
#---------------------------
# clear: permite borrar todos los elementos de una lista de una vez
#------------------
#lista1.clear()

#print(lista1)
#--------------
#Funciones / métodos de listas:
#- index: para buscar el índice de un elemento dentro de una lista

var = "Adios"
print(lista1.index(var))

# Iteracion de los elementos de la lista
listafor = [1, 2, 3, 4, 5]

for numero in listafor:
    print(numero)


#Acceder a indices y elementos de forma simultanea

#generamos una lista de fruta
frutas = ["manzana", "pera" , "platano"]

#Iteracion con indice y elementos
for indice, fruta in enumerate(frutas):
    print("Indice {}: {}".format(indice, fruta))


deseos = ["juegos", "joyas", "pelota", "ordenador"]

for i , papanoel in enumerate(deseos):
    print(f"Indice {i}: {papanoel}")



colores = ["rojo", "verde", "amarillo"]

for color in reversed(colores):
    print(color)

print("\n")

#Listas de notas

notas = [59, 14, 24, 91, 45]

#inicializar la suma de las notas

suma_notas = 0

#interar a traves de las notas y sumarlas

for nota in notas:
    suma_notas =+ nota

#Calcular el promedio
promedio = suma_notas / len(notas)

#Mostrar los resultados
print("notas de los estudiantes: ", notas)
print("La suma de las notas es: ", suma_notas)
print("promedio de las notas es: ", promedio)



