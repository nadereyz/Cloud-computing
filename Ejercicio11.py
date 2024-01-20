"""
 Crea un programa en Python que solicite al usuario introducir la temperatura en grados Celsius. Luego, realiza la conversión de esta temperatura a grados Fahrenheit utilizando la fórmula:

F=9/5⋅C+32

Donde *F* es la temperatura en grados Fahrenheit y *C* es la temperatura en grados Celsius.

Finalmente, muestra el resultado de la temperatura en ambas escalas. Utiliza f-strings para formatear la salida y muestra la temperatura en grados Fahrenheit con dos decimales.
 
 """


temperatura  = float(input("Inserta aqui el grado de temperatura\n"))

temperatura  = (9/5) * temperatura + 32

print(f"La temperatura en grado *C*: {temperatura:1.2f}")
print(f"La temperatura en grado Fahrenheit: {temperatura:1.2f}")
