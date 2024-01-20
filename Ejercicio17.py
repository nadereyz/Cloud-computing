"""
Crear un programa en Python que simule la gestión de las tareas pendientes. 

1. Utiliza una lista para almacenar las tareas y realiza las siguientes operaciones:
    1. Agregar tres tareas al final de la lista.
    2. Mostrar todas las tareas actuales
    3. Verificar si una tarea específica, tarea_buscar, está presente en vuestra lista
    4. Eliminar la segunda tarea de la lista
    5. Mostrar el número de tareas después de eliminar la del punto d.
"""
#1
tarea = ["limpiar", "ordenar", "recoger"]
#2
print(tarea)
#3
print(tarea.index("recoger"))
#4
tarea.remove("ordenar")
#5
print(tarea)
