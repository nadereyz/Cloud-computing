# Paso 1: Pregunta al usuario por su saldo inicial
saldo_inicial = float(input("Ingresa tu saldo inicial: "))

# Paso 2: Muestra un mensaje de bienvenida y el saldo inicial
print(f"Bienvenido/a. Tu saldo inicial es: {saldo_inicial}")

# Paso 3: Ingresar gastos
gastos = []
gasto = float(input("Ingresa el importe del primer gasto (o 0 para omitir): "))
saldo_inicial -= gasto
gastos.append(gasto)

# Paso 4: Ingresar ahorros
ahorros = []
ahorro = float(input("Ingresa el importe del primer ahorro (o 0 para omitir): "))
saldo_inicial += ahorro
ahorros.append(ahorro)

# Paso 5: Mostrar saldo actualizado y listas de gastos y ahorros
print(f"\nSaldo actualizado: {saldo_inicial}")
print("Lista de gastos:", gastos)
print("Lista de ahorros:", ahorros)
