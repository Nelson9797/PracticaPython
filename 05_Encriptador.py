palabra = str(input("Ingresa la palabra a encriptar: ")).upper()
encriptado = {"M":0, "U":1, "R": 2,"C":3, "I":4, "E":5, "L":6, "A":7, "G":8, "O":9}
palabra_encriptada = ""

for letra in palabra:
    if letra in encriptado.keys():
        palabra_encriptada = palabra_encriptada + str(encriptado.get(letra))
    else:
        palabra_encriptada = palabra_encriptada + letra

print(f"Palabra encriptada: {palabra_encriptada}")