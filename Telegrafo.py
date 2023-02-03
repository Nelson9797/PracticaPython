# Calcula cuanto costaria enviar un mensaje por telegrafo
# Las letras valen $1
# Los digitos valen $2
# Los caracteres especiales y letras del casellano (á é í ó ú ñ) valen $3

frase = str(input(" *"*7 + " Calculadora de Telegrafo " + "* "*7 + "\nIngresa la frase: "))
esp = ["ñ", "á", "é", "í", "ó", "ú", "Ñ", "Á", "É", "Í", "Ó", "Ú"]
precio = 0

for letra in frase:

    if letra.isdigit():
        precio += 2
    elif not letra.isspace():
        if not letra.isalnum() or letra in esp:
            precio += 3
        else:
            precio += 1

print(f"Precio del mensaje: ${precio}")