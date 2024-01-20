#*************** DICCIONARIOS
mi_diccionario_uno = {"nombre": "Juan", 'nombre2': 'María'}
mi_diccionario_dos = {"nombre": "Juan", "edad": "23", "Ciudad": "Málaga", "fecha_nacimiento": "12/13/2001"}
print(mi_diccionario_uno)
print(mi_diccionario_dos)

#Acceder a los elementos de un diccionario por clave
valor1 = mi_diccionario_uno["nombre"]
print(f"El nombre es {valor1}")  #Imprime: El nombre es Juan
valor2 = mi_diccionario_dos["edad"]
print(f"La edad es {valor2} años")   #Imprime: La edad es 23 años

#Modificar el valor de un elemento en un diccionario
mi_diccionario_uno["nombre"] = 'Pepe'
print("Diccionario modificado:\n", mi_diccionario_uno)

#Agregar un nuevo par clave-valor
contactos = {'Maria-Antonieta': '666666666',
             'Napoleón-Bonaparte': '99999999',
             'Francisco-Islas': '888888888'}

contactos["Paulo-Coello"] = "111111111"
print(contactos)

#Eliminar un par clave-valor existente en un diccionario
del contactos['Napoleón-Bonaparte']
print(contactos)

#Verificar si una clave existe en un diccionario
existe_Paulo_Coello = 'Alan Turing' in contactos
print(existe_Paulo_Coello)

#*******MÉTODOS MÁS COMUNES
claves = contactos.keys() #Obtener todas las claves
valores = contactos.values() #Obtener todos los valores
pares = contactos.items() #Obtener todos los pares clave-valor
print(claves)
print(valores)
print(pares)
contactos.pop('Maria-Antonieta')
del(contactos['Paulo-Coello'])
print(contactos)

#Imprimir todos los contactos utilizando utilizando un bucle for
print("Lista de mis mejores amigos:")
for nombre, telefono in contactos.items():
    print(f"{nombre}: {telefono}")

lista_contactos = contactos.items()

"""SINTAXIS BUCLE FOR --> 
colores = ["azul", "verde", "amarillo", "rojo"]
 
for color in colores:
     print(f"El siguiente color es {color})"""
     
     
#EJEMPLO DE PROGRAMA PARA GESTIONAR INFORMACIÓN DE ALUMNOS Y NOTAS

#Creamos un diccionario de estudiantes y notas
estudiantes = {
    'Joaquín': 10,
    'Gloria': 9,
    'Pepe': 8,
    'Bernardo': 7,
    'Ana': 6
}

#Creamos una función para agregar nuevos estudiantes
def agregar_estudiantes(nombre, calificacion):
    estudiantes[nombre] = calificacion
    print(f"El estudiante {nombre} ha sido agregado")


"""    
#Función para obtener la calificación de un estudiante
def obtener_calificacion(nombre):
    if nombre in estudiantes:
        return estudiantes[nombre]
    else:
        return None
"""
def obtener_calificacion(nombre):
    if nombre in estudiantes:
        return estudiantes[nombre]
    else:
        return None

#Obtener la calificación de un estudiante
calificacion_juana = obtener_calificacion('Alicia')
print(calificacion_juana)
    
#Imprimir todas las calificaciones
def imprimir_calificaciones():
    print("Calificaciones de estudiantes:")
    for nombre, calificacion in estudiantes.items():
        print(f"{nombre}: {calificacion}")

#Imprimir estudiantes
print(estudiantes)

#Agregar un nuevo estudiante
agregar_estudiantes('Juana', 3)
print(estudiantes)

#Modificar la nota de un estudiante
agregar_estudiantes('Juana', 4)
print(estudiantes)

calificacion_juana = obtener_calificacion('Juana')
print(f"La calificación de Juana es: {calificacion_juana}")

imprimir_calificaciones()