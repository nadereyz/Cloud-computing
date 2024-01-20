"""




"""

# usuario 1
usuario1_nombre = "Alice"
usuario1_correo = "alice@email.com"

# usuario 2
usuario2_nombre = "Bob"
usuario2_correo = "bob@email.com"

# Verificar
usuario_actual = "Alice"

# verificar de usuarios
esta_registrado = usuario_actual in [usuario1_nombre, usuario2_nombre]
print(f"Usuario '{usuario_actual}' está registrado: {esta_registrado}")

# Comprobación de Correo Electrónico
mismo_correo = usuario1_correo == usuario2_correo
print(f"Ambos usuarios comparten el mismo correo electrónico: {mismo_correo}")

# Identificación de Objetos
objetos_diferentes = usuario1_nombre is not usuario2_nombre or usuario1_correo is not usuario2_correo
print(f"Los objetos que representan a los usuarios son diferentes: {objetos_diferentes}")
