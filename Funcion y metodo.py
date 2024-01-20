#**********************FUNCIÓN --> BLOQUE DE CÓDIGO QUE REALIZA UNA FUNCiÓN : PUEDE SER DEFINIDO CON DEF. 

# Definimos la función y la tarea específica que realiza
# Especificamos el resultado que nos debe devolver
def suma_dos(a, b):
    return a + b 

#utilizamos la función
resultado = suma_dos(3, 4) 

#imprimimos el resultado
print(resultado)

# Definimos la función y la tarea específica que realiza
# Especificamos el resultado que nos debe devolver
def suma_tres(a, b, c):
    return a + b + c

#utilizamos la función
resultado_tres = suma_tres(3, 4, 10)

#imprimimos el resultado
print(resultado_tres)

#**********************MÉTODOS: funciones que estan asociadas a un objeto específico y que se llaman en ese objetos

lista_uno = [1, 2, 3]

lista_uno.index(2) #sintaxis objeto.metodo()

#**********************TUPLAS: Secuencias ordenadas INMUTABLES

mi_lista = [1, 2, 3, 4] #Colecciones de elementos que sí pueden cambiar
mi_tupla = (1, 2, 3, 4, 5, 6) #Colecciones de elementos que no pueden cambiar

print(mi_tupla[2])

mi_lista[0] = 10
#mi_tupla[0] = 10 --> Error TypeError: una tupla no permite la reasignación de elementos.

print(mi_lista, mi_tupla)

# MÉTODOS MÁS COMUNES: count(), index(), len()

#Count: Este método cuenta cuántas veces aparece un valor específico en la tupla
mi_tupla_dos = (1, 2, 2, 2, 3, 2, 4)
print(mi_tupla_dos.count(2))

#Index: Nos devuelve el índice de la primera aparición del valor en la tupla
print(mi_tupla_dos.index(2)) #Sintaxis: objeto.metodo(valor)

#Len: Devuelve el número de elementos de la tupla
print(len(mi_tupla_dos)) # Sintaxis de función: método(objeto)

# FUNCIONES MÁS COMUNES: max(), min(), sum(), sorted()

#Max: Devuelve el valor máximo dentro de una tupla
mi_tupla_tres = (5, 4, 8, 10, 22)
print(max(mi_tupla_tres)) #Sintaxis de función: función(objeto) 

#Min: Devuelve el valor mínimo dentro de una tupla
print(min(mi_tupla_tres)) #Sintaxis de función: función(objeto) 

#Sum:suma de los elementos
print(sum(mi_tupla_tres)) #Sintaxis de función: función(objeto) 

#Sorted: Crea una tupla ordenada a partir de la tupla original
print(tuple(sorted(mi_tupla_tres))) #Imprimo la tupla mi_tupla_tres ordenada

tupla_ordenada = tuple(sorted(mi_tupla_tres)) # Creo una nueva tupla con los valores de mi_tupla_tres
print(tupla_ordenada)

tupla_string = ("perro", "gato", "pajaro", "rana")
print(tuple(sorted(tupla_string))) #Ordena los strings alfabéticamente


#**********************CONJUNTOS: Colecciones desordenadas de elementos únicos

mi_conjunto = {4, 2, 3, 1, 2, 4} #No hay un orden específico y no puede haber elementos duplicados
print(mi_conjunto)

#Operaciones de conjunto para combinar o comparar conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

#Unión
union = conjunto1 | conjunto2
print(union)

#Intersección
interseccion = conjunto1 & conjunto2
print(interseccion)

#Diferencia
diferencia = conjunto1 - conjunto2
print(diferencia)

#Ejemplo Campaña MKT Digital Keywords & Hashtag Asociados
viajes = {"viajes romanticos", "viajes fin de curso", "viajes baratos"}
viajar = {"viajes romanticos", "viajes baratos"}
vuelos = {"viajes fin de curso", "viajes baratos"}

hastag_campania_instagram = viajes | viajar | vuelos
print(hastag_campania_instagram)


#Función set(): Crear un conjunto vacio o un conjunto a partir de otra colección
conjunto_vacio = set()
print(conjunto_vacio)
conjunto_desde_lista = set([1, 2, 3])
print(conjunto_desde_lista)

#Método add(): agregar elementos a mi conjunto
mi_conjunto_add = {1, 10, 3}
mi_conjunto_add.add(4)
print(mi_conjunto_add)

#Método remove(): Eliminar un elemento específico del conjunto. 
#mi_conjunto_add.remove(4) KeyError porque el valor 4 no se encuentra entre los valores de mi_conjunto_add
mi_conjunto_add.remove(10)
print(mi_conjunto_add)

#Método discard(): Similar a remove pero no genera error si el elemento no está presente
mi_conjunto_discard = {2, 23, 45, 12, 50, 66, 13}
mi_conjunto_discard.discard(45)
print(mi_conjunto_discard)

socios_club_tenis = {"juan pedro", "maría rosina", "pepe flores"} 
socios_club_tenis.discard("elena sofía")
print(socios_club_tenis)

#Método union(): unir dos conjuntos ignorando los valores repetidos
conjunto_union_uno = {1, 2, 3}
conjunto_union_dos = {3, 4, 5}
union_conjuntos = conjunto_union_uno.union(conjunto_union_dos) # conjunto_union_uno | conjunto_union_dos
print(union_conjuntos)

#Método intersection(): Devuelve un nuevo conjunto con valores comunes entre ambos conjuntos
conjunto_interseccion_uno = {1, 2, 3}
conjunto_interseccion_dos = {3, 4, 5}
union_conjuntos_dos = conjunto_interseccion_uno.intersection(conjunto_interseccion_dos) # conjunto_interseccion_uno & conjunto_interseccion_dos
print(union_conjuntos_dos)

#Método difference(): Evalua el primer conjunto y nos devuelve los valores del primer conjunto que no se repiten en el segundo conjunto
conjunto_diferencia_uno = {1, 2, 3}
conjunto_diferencia_dos = {3, 4, 5}
union_conjuntos_tres = conjunto_diferencia_uno.difference(conjunto_diferencia_dos) # conjunto_interseccion_uno - conjunto_interseccion_dos
print(union_conjuntos_tres)