"""
Crea un programa en Python que solicite al usuario ingresar su año de nacimiento y el año actual. Utiliza esta información para calcular su edad actual y edad futura.

1. Solicita al usuario que introduzca su año de nacimiento.
2. Solicita al usuario que introduzca el año actual.

Luego, realiza los siguientes cálculos:

- Calcula la edad actual restando el año de nacimiento del año actual.
- Calcula la edad que tendría en 5 años sumando 5 a la edad actual.
- Calcula la edad que tendría en 10 años sumando 10 a la edad actual.

Finalmente, utiliza la función **`print()`** para mostrar un mensaje que incluya la información de la siguiente manera:

¡Bienvenido a la Calculadora de Edades!

Introduce tu año de nacimiento: 1990
Introduce el año actual: 2023

Resultados:

- Tienes 33 años, ¡Aún te queda muchas cosas buenas por vivir!
- En 5 años tendrás 38 años.
- En 10 años tendrás 43 años.
"""

print("Bienvenido a la calculadora de edades!\n")

fecha = float(input("Ingresa tu año de nacimiento: \n"))
edadactual = int(input("Ingresa tu año actual: \n"))

edadactual = edadactual - fecha

edad5 = edadactual + 5

edad10 = edadactual + 10

print("\n RESULTADOS! \n")

print(f"Tienes {edadactual} años, ¡Aún te quedan muchas cosas buenas por vivir!")
print(f"En 5 años tendrás {edad5} años.")
print(f"En 10 años tendrás {edad10} años.")

"""
# CODIGO MAS OPTIMIZADO

#programa de informacion personal
print(" bienvenido al programa de informacion perosnal")

#entrada de datos
nombreop = input("Introduce tu nombre")
edadop = input("Introduce tu edad")
ciudadop = input("Introduce tu ciudad")

#mensaje personalizada usando .format()
mensaje_format = "Hola, {}! bienvenido a {}. ".format(nombreop,ciudadop)
mensaje_fstring = f"Esperamos que disfrutes tu estada. Tienes {edadop} años de sabiduria. "

#mostrar resultados
print(mensaje_format)
print(mensaje_fstring)
"""



