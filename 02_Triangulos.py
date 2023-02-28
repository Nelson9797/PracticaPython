# Comprueba si los 3 lados introducidos son validos para un triangulo
# Cualquier lado no debe de ser mas grande que la suma de los otros dos

a, b, c = int(input("Ingresa el lado A: ")), int(input("Ingresa el lado C: ")), int(input("Ingresa el lado C: "))
if((a < (b + c)) and (b < (a + c)) and (c < (a + b))):
    print("El triangulo es valido")
else:
    print("El triangulo es invalido")
