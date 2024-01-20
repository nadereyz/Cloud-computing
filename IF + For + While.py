#****************** CONDICIONALES#*********************** BUCLES
"""Los bucles son estructuras que permiten repetir una o varias instrucciones un número determinado de veces, o hasta que se cumpla una condición"""
#Bucle For
frutas = ["manzana", "pera", "melón"]
for fruta in frutas:
    print(fruta)

#Ejemplo bucle for con un rango numérico
for i in range(5): # i --> index
    print(i) #Me va a imprimir los elementos del 0 al 4, hasta que llegue al límite del rango que es 5. io toma el valor de cada número en la interacción
animales = ["perro", "gato", "lagarto", "camaleón"]
for animales in range(2):
    print(animales)

#Bucle WHILE
"""Se ejecuta mientras la condición sea verdadera"""
contador = 6
while contador < 5:
    print("contador es menor que 5")

# ejemplo de passowrd con while y if
intento_max = 3
intento_realizado = 0

while True:
    usuario = input("pon tu contraseña: ")

    if usuario == "contraseña":
        print("es correcto la pass")
        break
    
    print("Vuelve a introduccir la pass")
    intento_realizado +=1

    if intento_realizado == intento_max:
        print("has agotado ya")
        break

#****************** CONDICIONALES
numero = 4
def especificar_numero():
    if numero > 5:
        print("El numero es mayor que 5")
    else:
        print("El numero es menor que 5")

especificar_numero()
#Ejemplo de temperatura 
temperatura = float(input("Introduce la temperatura en Celsius:\n"))

if temperatura < 10:
    print('Hace un frio del carajo')
elif  10 <= temperatura <= 25:
    print('No hace mal tiempo')
else:
    print('Hace calor')