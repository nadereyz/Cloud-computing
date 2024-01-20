"""
Crea un programa en Python que simule la evaluación de condiciones utilizando operadores lógicos. Utiliza variables para representar las siguientes situaciones:

1. Un estudiante ha aprobado si su puntuación es mayor o igual a 60.
2. Un usuario tiene acceso si es un administrador o tiene una suscripción premium.
3. Un número es positivo si es mayor que 0 y menor que 100.
4. Un equipo gana si ha anotado más de 3 goles y no ha recibido ningún gol en contra.

Utiliza operadores lógicos (**`and`**, **`or`**, **`not`**) para evaluar estas condiciones y muestra el resultado de cada situación utilizando la función **`print()`**.

*Ejemplo de salida:*

*Puntuación del estudiante: 75
El estudiante ha aprobado: True*

*Usuario es administrador: True
Usuario tiene suscripción premium: False
El usuario tiene acceso: True*

*Número a evaluar: 45
El número es positivo: True*

*Goles a favor: 4
Goles en contra: 0
El equipo ha ganado: True*
"""
# 1
puntuaciones = 75
aprobado = puntuaciones >= 60
print("Puntuacion del estudiante: " , puntuaciones)
print("El estudiante ha aprobado: " , aprobado , "\n" )

# 2
administrador = True
subpremium = False
acceso_usuario = administrador or subpremium
print("Usuario es administrador:", administrador)
print("Usuario tiene suscripción premium:", subpremium)
print("El usuario tiene acceso:", acceso_usuario, "\n")

# 3
numeroaleatorio = 45
numpositivo = 0 < numeroaleatorio < 100
print("Número a evaluar:", numeroaleatorio)
print("El número es positivo:", numpositivo, "\n")

# 4
goles_a_favor = 4
goles_en_contra = 0
equipo_gana = goles_a_favor > 3 and goles_en_contra == 0
print("Goles a favor:", goles_a_favor)
print("Goles en contra:", goles_en_contra)
print("El equipo ha ganado:", equipo_gana)