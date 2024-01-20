"""
Vamos a crear un programa que utilice tuplas y las funciones/métodos que hemos explorado. Este programa simulará un registro de compras mensuales y realizará varias operaciones utilizando tuplas.

1. Crea una tupla llamada **`compras_enero`** que contenga los precios de productos comprados durante el mes de enero.
2. Crea una función llamada **`calcular_total`** que acepte una tupla de precios y devuelva el total gastado en compras.
3. Implementa una función llamada **`producto_mas_caro`** que acepte una tupla de precios y devuelva el precio del producto más caro.
4. Crea una tupla llamada **`compras_febrero`** con precios de productos comprados en febrero.
5. Utiliza el método **`count`** para contar cuántas veces se compró un producto específico en febrero.
6. Utiliza la función **`max`** para encontrar el precio más alto entre las dos tuplas.
7. Utiliza la función **`sum`** para calcular el gasto total en ambos meses.
8. Utiliza la función **`sorted`** para obtener una tupla ordenada de precios en ambos meses.
9. Imprime los resultados de las operaciones anteriores.
"""

# 1
compras_enero = (24, 3, 17, 99, 50)
print("Compras de enero:", compras_enero)

# 2
def calcular_total(precios):
    return sum(precios)
print("Total gastado en enero:", calcular_total(compras_enero))

# 3
def producto_mas_caro(precios):
    return max(precios)
print("Producto más caro en enero:", producto_mas_caro(compras_enero))

# 4
compras_febrero = (10, 23, 4, 21, 41, 4, 4)
print("Compras de febrero:", compras_febrero)

# 5
producto_especifico = 4
veces_comprado_febrero = compras_febrero.count(producto_especifico)
print("Producto específico comprado en febrero {} veces.".format(veces_comprado_febrero))

# 6
precio_mas_alto = max(compras_enero + compras_febrero)
print("Precio más alto entre enero y febrero:", precio_mas_alto)

# 7
gasto_total = sum(compras_enero + compras_febrero)
print("Gasto total en ambos meses:", gasto_total)

# 8
precios_ordenados = sorted(compras_enero + compras_febrero)
print("Precios ordenados en ambos meses:", precios_ordenados)





















