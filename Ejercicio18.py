"""
Crea un programa en Python que simule el registro de gastos y ahorros. Utiliza variables para representar el saldo inicial, 
solicita al usuario ingresar gastos y ahorros, y utiliza operadores y el método **`append()`** para actualizar la información.
Realiza las siguientes operaciones:

1. Pregunta al usuario por su saldo inicial utilizando **`input()`**.
2. Muestra un mensaje de bienvenida y el saldo inicial.
3. Pregunta al usuario por el importe de un gasto y lo resta del saldo.
4. Pregunta al usuario por el importe de un ahorro y lo suma al saldo.
5. Muestra el saldo actualizado y una lista con los gastos y ahorros registrados.
"""

#1
usuario_saldo = int(input("Introduce tu saldo inicial: "))
#2
print("Tu saldo inicial es:", usuario_saldo)

#3
gastos = []
gastoingreso = int(input("Pon tu ingreso del primer gasto: "))
gastos.append(gastoingreso)
restarsueldo = usuario_saldo - gastoingreso
print("Tienes el saldo: ", restarsueldo)

#4
ahorros = int(input("Pon tu ingreso del primer ahorro: "))
registroahorro = []
registroahorro.append(ahorros)

#5

print(f"El gasto actualizado es: {gastos}")
print(f"El saldo actualizado es: {registroahorro}")