"""
Vamos a crear un programa sencillo utilizando diccionarios y la función **`input`** 
para registrar las calificaciones de estudiantes. El programa debe hacer lo siguiente:

1. Solicitar al usuario que ingrese el nombre de un estudiante y su calificación.
2. Verificar si el estudiante ya está registrado. Si está registrado, preguntar al usuario si desea actualizar la calificación.
3. Imprimir el registro completo de calificaciones.
"""

notas = {}
nombre_estudiante = input("Pon tu nombre: ")
notas_estudiante = float(input("Pon tu nota: "))

def registrar_calificacion():
    
    
    if nombre_estudiante in notas:
        update = input("¿Quieres actualizar tu nota? (si/no): ")       
        if update == "si":
            notas[nombre_estudiante] = notas_estudiante
    else:
        notas[nombre_estudiante] = notas_estudiante


print("\nRegistro completo de calificaciones:")
for estudiante, calificacion in notas.items():
    print(f"{estudiante}: {calificacion}")




