
sueldo = float(input("Introduce el sueldo ofrecido: "))

sueldo = sueldo % 21

if sueldo < 1000:
    print("El sueldo un poco bajo")
elif sueldo < 2000:
    print("El sueldo no esta mal")
elif sueldo < 3000:
    print("madre mia pero donde vas")
else:
    print("O has equivocado un numero o eres millonario!")


